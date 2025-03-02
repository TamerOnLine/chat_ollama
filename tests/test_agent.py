import pytest
import os
from agent.agent import Agent

@pytest.fixture
def agent():
    return Agent()

@pytest.mark.skipif(
    os.getenv("DISABLE_OLLAMA", "false").lower() == "true",
    reason="Ollama is disabled in CI/CD"
)
def test_agent_process(agent):
    response = agent.process("What is the weather in Berlin?")
    assert isinstance(response, str)
