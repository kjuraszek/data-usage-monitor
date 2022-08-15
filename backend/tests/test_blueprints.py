"""
Set of tests for backend.application.blueprints
"""

def test_api_bp(client):
    response = client.get('/api/')
    assert response.status_code == 200
    assert b'<title>Data Usage Monitor API</title>' in response.data


def test_api_bp_unallowed(client):
    response = client.post('/api/')
    assert response.status_code == 405
    assert b'<title>405 Method Not Allowed</title>' in response.data
