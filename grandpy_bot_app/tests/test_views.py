#!/usr/bin/python3
# -*- coding: Utf-8 -*-

from flask import Flask, request
from grandpy_bot_app.views import app
from grandpy_bot_app.parser import Parser
import pytest


user_question = "Bonjour, ou se trouve la Tour Eiffel ?"

@pytest.fixture(scope='session')
def client():
    app.config['TESTING'] = True
    return app.test_client()

# We test server load index.html when user get / url
def test_home_page(client):
    rsp = client.get('/')
    html = rsp.get_data(as_text=True)
    assert rsp.status == '200 OK'
    assert '<title>GrandPy</title>' in html

