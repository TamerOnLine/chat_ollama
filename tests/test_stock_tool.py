import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.tools.stock_tool import get_stock_price

def test_stock_tool():
    response = get_stock_price("AAPL")
    assert isinstance(response, str)
    assert "USD" in response or "error" in response.lower()
