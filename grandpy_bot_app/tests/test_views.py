from flask import Flask
from grandpy_bot_app.views import app
import pytest


@pytest.fixture(scope='session')
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home_page(client):
    rsp = client.get('/')
    assert rsp.status == '200 OK'
    html = rsp.get_data(as_text=True)
    assert '<title>GrandPy</title>' in html
