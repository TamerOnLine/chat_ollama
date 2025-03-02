import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.main import main

def test_main_script():
    assert callable(main)  # Check if the main function exists
