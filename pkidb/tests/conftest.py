import base64
import json

import pytest
import rsa

from pkidb.api import app

RSA_KEYSIZE = 1024
public_key, private_key = rsa.newkeys(RSA_KEYSIZE)


@pytest.fixture()
def client():
    """Return test client for Flask application."""
    return app.test_client()


@pytest.fixture()
def payload():
    """Return payload data to use for testing."""
    key = "test_key"
    value = json.dumps([1, 2, 3])
    signature = base64.b64encode(
        rsa.sign(value.encode(), private_key, "SHA-256")
    ).decode()
    payload = {
        "key": key,
        "value": value,
        "n": public_key.n,
        "e": public_key.e,
        "signature": signature,
    }
    return payload
