import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
import requests
from get_weather_data import fetch_weather_data 


class MockResponse:
    @staticmethod
    def json():
        return {
            "daily": [
                {"temp": {"max": 20, "min": 15}, "weather": [{"description": "clear sky"}], "wind_speed": 5},
                {"temp": {"max": 22, "min": 16}, "weather": [{"description": "partly cloudy"}], "wind_speed": 6}
            ]
        }

    @staticmethod
    def raise_for_status():
        pass  

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch('requests.get', return_value=MockResponse())

def test_fetch_weather_data(mock_requests_get):
    lat, lon = 59.334591, 18.063240
    data = fetch_weather_data(lat, lon)
    assert "daily" in data
    assert len(data["daily"]) > 0
    assert data["daily"][0]["temp"]["max"] == 20

# print("Test for fetch_weather_data was successful")