"""
Set of tests for backend root URL
"""

def test_index(client):
    response = client.get('/')
    assert response.status_code == 404
