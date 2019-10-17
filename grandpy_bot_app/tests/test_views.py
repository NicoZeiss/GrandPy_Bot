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

# We test that user input is posted and sent to our parser
def test_user_post(client):
	rv = client.post('/question', data=dict(question=user_question), follow_redirects=True)
	parser = Parser(user_question)
	assert b'Bonjour, ou se trouve la Tour Eiffel ?' in rv.data
	assert parser.user_input == "bonjour, ou se trouve la tour eiffel ?"


	
