"""
Sensor for the Nextbike data.

For more details about this platform, please refer to the documentation at
https://github.com/syssi/nextbike
"""
import asyncio
from datetime import timedelta
import logging

import aiohttp
import async_timeout
import voluptuous as vol

from homeassistant.components.sensor import ENTITY_ID_FORMAT, PLATFORM_SCHEMA
from homeassistant.const import (
    ATTR_ATTRIBUTION, ATTR_ID, ATTR_LATITUDE, ATTR_LOCATION, ATTR_LONGITUDE,
    ATTR_NAME, CONF_LATITUDE, CONF_LONGITUDE, CONF_NAME, CONF_RADIUS,
    LENGTH_FEET, LENGTH_METERS)
from homeassistant.exceptions import PlatformNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity, async_generate_entity_id
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.util import distance, location

_LOGGER = logging.getLogger(__name__)

PLATFORM = 'nextbike'

ATTR_PLACES = 'places'
ATTR_CITIES = 'cities'
ATTR_COUNTRIES = 'countries'

CONF_CITY_ID = 'city_id'

DEFAULT_ENDPOINT = 'https://api.nextbike.net/{uri}'
MAPS_URI = 'maps/nextbike-live.json?&city={city}'

REQUEST_TIMEOUT = 5  # In seconds; argument to asyncio.timeout

SCAN_INTERVAL = timedelta(minutes=5)  # Timely, and doesn't suffocate the API

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_CITY_ID): cv.positive_int,
    vol.Required(CONF_RADIUS, default=500): cv.positive_int,
    vol.Optional(CONF_NAME, default='nextbike'): cv.string,
    vol.Inclusive(CONF_LATITUDE, 'coordinates'): cv.latitude,
    vol.Inclusive(CONF_LONGITUDE, 'coordinates'): cv.longitude,
})

PLACE_SCHEMA = vol.Schema({
    vol.Required('uid'): cv.positive_int,
    vol.Required('lat'): cv.latitude,
    vol.Required('lng'): cv.longitude,
    vol.Required('name'): cv.string,
    vol.Required('bikes'): cv.positive_int,
    vol.Required('place_type'): cv.positive_int,
    vol.Required('terminal_type'): cv.string,
}, extra=vol.REMOVE_EXTRA)

CITY_SCHEMA = vol.Schema({
    vol.Required(ATTR_PLACES): [PLACE_SCHEMA],
}, extra=vol.REMOVE_EXTRA)

COUNTRY_SCHEMA = vol.Schema({
    vol.Required(ATTR_CITIES): [CITY_SCHEMA],
}, extra=vol.REMOVE_EXTRA)

MAPS_RESPONSE_SCHEMA = vol.Schema({
    vol.Required(ATTR_COUNTRIES): [COUNTRY_SCHEMA]
})


class NextbikeRequestError(Exception):
    """Error to indicate a Nextbike API request has failed."""
    pass


async def async_nextbike_request(hass, uri, schema):
    """Perform a request to Nextbike API endpoint, and parse the response."""
    try:
        session = async_get_clientsession(hass)

        with async_timeout.timeout(REQUEST_TIMEOUT, loop=hass.loop):
            req = await session.get(DEFAULT_ENDPOINT.format(uri=uri))

        json_response = await req.json()
        return schema(json_response)
    except (asyncio.TimeoutError, aiohttp.ClientError) as ex:
        _LOGGER.error("Could not connect to Nextbike API endpoint: %s", ex)
    except ValueError as ex:
        _LOGGER.error("Received non-JSON data from Nextbike API endpoint: %s", ex)
    except vol.Invalid as ex:
        _LOGGER.error("Received unexpected JSON from Nextbike API endpoint: %s", ex)
    raise NextbikeRequestError


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Nextbike platform."""
    if PLATFORM not in hass.data:
        hass.data[PLATFORM] = {}

    city_id = config.get(CONF_CITY_ID)
    latitude = config.get(CONF_LATITUDE, hass.config.latitude)
    longitude = config.get(CONF_LONGITUDE, hass.config.longitude)
    radius = config.get(CONF_RADIUS)
    name = config.get(CONF_NAME)
    if not hass.config.units.is_metric:
        radius = distance.convert(radius, LENGTH_FEET, LENGTH_METERS)

    if city_id not in hass.data[PLATFORM]:
        city = NextbikeCity(hass, city_id)
        hass.data[PLATFORM][city_id] = city
        hass.async_add_job(city.async_refresh)
        async_track_time_interval(hass, city.async_refresh, SCAN_INTERVAL)
    else:
        city = hass.data[PLATFORM][city_id]

    await city.ready.wait()

    async_add_entities([NextbikeSensor(hass, city, radius, latitude, longitude, name)], True)


class NextbikeCity:
    """Thin wrapper around a Nextbike city object."""

    def __init__(self, hass, city_id):
        """Initialize the city object."""
        self.hass = hass
        self.city_id = city_id
        self.places = []
        self.ready = asyncio.Event()

    async def async_refresh(self, now=None):
        """Refresh the state of the network."""
        try:
            city = await async_nextbike_request(self.hass, MAPS_URI.format(city=self.city_id), MAPS_RESPONSE_SCHEMA)
            self.places = city[ATTR_COUNTRIES][0][ATTR_CITIES][0][ATTR_PLACES]
            self.ready.set()
        except NextbikeRequestError:
            if now is not None:
                self.ready.clear()
            else:
                raise PlatformNotReady


class NextbikeSensor(Entity):
    """CityBikes API Sensor."""

    def __init__(self, hass, city, radius, latitude, longitude, name):
        """Initialize the sensor."""
        self._city = city
        self._radius = radius
        self._latitude = latitude
        self._longitude = longitude
        self._name = name
        self._state = None

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    async def async_update(self):
        """Update sensor state."""
        if self._city.ready.is_set():
            available_bikes = 0
            for place in self._city.places:
                distance = location.distance(self._latitude, self._longitude, place['lat'], place['lng'])
                if distance < self._radius:
                    available_bikes += place['bikes']
            self._state = available_bikes

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return 'bikes'

    @property
    def icon(self):
        """Return the icon."""
        return 'mdi:bike'
