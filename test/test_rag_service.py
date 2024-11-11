from unittest.mock import MagicMock
from rag_service import handle_query, rag_agent

def test_handle_query_success():
    query = "What is soccer?"
    # mock_response = "Soccer is a popular sport."

    response = handle_query(query)
    assert isinstance(response, str)
    assert response != ""

def test_handle_query_empty_response():
    query = "Undefined question"

    response = handle_query(query)
    assert isinstance(response, str)
