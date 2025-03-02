import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.agent.agent import Agent

@pytest.fixture
def agent():
    return Agent()

def test_agent_process(agent):
    response = agent.process("What is the weather in Berlin?")
    assert isinstance(response, str)
