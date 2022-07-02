"""
Set of fixtures for application.
"""
import pytest
from backend.application import init_app


@pytest.fixture()
def app():
    app = init_app()
    app.config.update({
        'TESTING': True,
        'PRESERVE_CONTEXT_ON_EXCEPTION': False
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
