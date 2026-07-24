"""Tests for the Nextbike sensor.

The fixtures under ``tests/fixtures`` are trimmed excerpts of the official
``nextbike-live.json`` API response for Leipzig (1), Berlin (362) and Linz
(692). Each keeps a near cluster of stations plus two far ones so radius
filtering can be asserted independently of the exact distance formula.
"""

import asyncio
from types import SimpleNamespace

from homeassistant.setup import async_setup_component
import pytest

from custom_components.nextbike.sensor import (
    ATTR_CITIES,
    ATTR_CLOSEST_BIKES,
    ATTR_CLOSEST_DISTANCE,
    ATTR_COUNTRIES,
    ATTR_E_BIKES,
    ATTR_PLACES,
    MAPS_RESPONSE_SCHEMA,
    NextbikeSensor,
)

from .conftest import load_fixture

CITY_IDS = [1, 362, 692]

LEIPZIG_CLOSEST = (
    "20390,20304,190469,190410,23460,23242,23191,20501,39138,39111,20329,20380,"
    "300010,59993,21527,21575,21810,21839,21844,59858,59830,59814,20136,23591,"
    "20391,23237,23392,350522,190390,190443,190252,190243,190226,190287,190289"
)
BERLIN_CLOSEST = "18890,18649,18531,17686,16837,14755,15328,19645,100848,100381,10579,13686"
LINZ_CLOSEST = "390386,390377,390270,390263,390192,390125,390090,390064,390031,390028,390018,390002"

# city_id, latitude, longitude, radius, bikes, e_bikes, closest_bikes
SCENARIOS = [
    (1, 51.34366, 12.37879, 25, 35, 4, LEIPZIG_CLOSEST),
    (1, 51.34366, 12.37879, 500, 37, 4, LEIPZIG_CLOSEST),
    (1, 51.34366, 12.37879, 60000, 39, 5, LEIPZIG_CLOSEST),
    (362, 52.50281, 13.48485, 500, 14, 0, BERLIN_CLOSEST),
    (362, 52.50281, 13.48485, 60000, 16, 0, BERLIN_CLOSEST),
    (692, 48.30319, 14.28932, 500, 21, 0, LINZ_CLOSEST),
    (692, 48.30319, 14.28932, 60000, 37, 0, LINZ_CLOSEST),
]


def parse_places(city_id):
    """Validate a fixture against the API schema and return its places."""
    response = MAPS_RESPONSE_SCHEMA(load_fixture(city_id))
    return response[ATTR_COUNTRIES][0][ATTR_CITIES][0][ATTR_PLACES]


def ready_city(places):
    """Build a minimal ready city stand-in holding parsed places."""
    event = asyncio.Event()
    event.set()
    return SimpleNamespace(ready=event, places=places)


@pytest.mark.parametrize("city_id", CITY_IDS)
def test_fixtures_match_schema(city_id):
    """The official API response shape validates and exposes places."""
    assert parse_places(city_id)


@pytest.mark.parametrize(
    "city_id,latitude,longitude,radius,bikes,e_bikes,closest",
    SCENARIOS,
)
async def test_sensor_state(
    city_id, latitude, longitude, radius, bikes, e_bikes, closest
):
    """Sensor state and attributes match the configured location and radius."""
    city = ready_city(parse_places(city_id))
    sensor = NextbikeSensor(None, city, radius, latitude, longitude, "nextbike")

    await sensor.async_update()

    assert sensor.state == bikes
    attrs = sensor.extra_state_attributes
    assert attrs[ATTR_E_BIKES] == e_bikes
    assert attrs[ATTR_CLOSEST_BIKES] == closest
    assert isinstance(attrs[ATTR_CLOSEST_DISTANCE], int)
    assert attrs[ATTR_CLOSEST_DISTANCE] < radius


async def test_setup_platform(hass, aioclient_mock):
    """Setting up the platform exposes an entity with the expected state."""
    aioclient_mock.get(
        "https://maps.nextbike.net/maps/nextbike-live.json?&city=692",
        json=load_fixture(692),
    )
    config = {
        "sensor": {
            "platform": "nextbike",
            "city_id": 692,
            "radius": 500,
            "latitude": 48.30319,
            "longitude": 14.28932,
            "name": "linz",
        }
    }

    assert await async_setup_component(hass, "sensor", config)
    await hass.async_block_till_done()

    state = hass.states.get("sensor.linz")
    assert state is not None
    assert state.state == "21"
    assert state.attributes[ATTR_E_BIKES] == 0
