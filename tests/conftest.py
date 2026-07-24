"""Fixtures for the Nextbike tests."""

import json
from pathlib import Path

import pytest

FIXTURE_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable loading of the custom component in every test."""
    yield


def load_fixture(city_id):
    """Return the parsed API response fixture for a city."""
    return json.loads((FIXTURE_DIR / f"city_{city_id}.json").read_text())
