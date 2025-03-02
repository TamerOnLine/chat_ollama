import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.tools.weather_tool import get_weather

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
assert API_KEY is not None, "API_KEY is missing. Please check your environment variables."


def test_weather_tool():
    response = get_weather("Berlin")
    assert isinstance(response, str)
    assert "temperature" in response.lower() or "error" in response.lower()
