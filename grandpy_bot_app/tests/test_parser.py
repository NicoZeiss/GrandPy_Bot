#!/usr/bin/python3
# -*- coding: Utf-8 -*-

from flask import Flask
import grandpy_bot_app.parser as script
import pytest




class TestParser:
	user_question = "Bonjour, ou se trouve la Tour Eiffel ?"
	INPUT = script.Parser(user_question)

	# We test that parser receive a string with user input
	def test_user_input(self):
		assert self.INPUT.user_input == "bonjour, ou se trouve la tour eiffel ?"

	# We test that parser split the user input and delete punctuation
	def test_parse(self):
		self.INPUT.parse()
		parsed_input = self.INPUT.parsed_input
		assert parsed_input == ['tour', 'eiffel']




	
