import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.tools.custom_tool import custom_response_tool

def test_custom_tool():
    response = custom_response_tool("Random query")
    assert isinstance(response, str)
    assert "Sorry" in response or "response" in response.lower()
