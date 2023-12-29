def test_set(client, payload):
    """Test setting a value with the API."""
    value = client.get("/set/", json=payload).json
    assert value == payload["value"]


def test_get(client, payload):
    """Test getting a value with the API."""
    value = client.get("/get/", json=payload).json
    assert value == payload["value"]
