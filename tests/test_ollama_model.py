import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.model.ollama_model import OllamaHandler

@pytest.fixture
def ollama_handler():
    return OllamaHandler()

def test_ollama_model_call(ollama_handler):
    response = ollama_handler.explain_question_mark("Tell me a fact about AI.")
    assert isinstance(response, str)
