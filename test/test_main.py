import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_index_get():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_query_rag_success():
    query_data = {"query": "What is soccer?"}
    response = client.post("/query", json=query_data)
    assert response.status_code == 200
    assert "response" in response.json()

def test_query_rag_failure():
    query_data = {"query": "Faulty query"}
    with pytest.raises(Exception):
        response = client.post("/query", json=query_data)
        assert response.status_code == 500

def test_websocket_query():
    with client.websocket_connect("/ws/query") as websocket:
        # Send a test query message
        test_query = "What's the latest on soccer?"
        websocket.send_text(test_query)

        try:
            # Receive the response from the WebSocket endpoint
            response = websocket.receive_json()  # Expect JSON format as per your WebSocket setup

            assert "response" in response
            assert isinstance(response["response"], str)
            assert len(response["response"]) > 0  # Ensure it’s not an empty response

        except WebSocketDisconnect as e:
            pytest.fail(f"WebSocket disconnected unexpectedly with code: {e.code}")
