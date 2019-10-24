#!/usr/bin/python3
# -*- coding: Utf-8 -*-

from flask import Flask
import grandpy_bot_app.parser as script
import pytest




class TestParser:
	punct = ",?.:!"
	apost = "l'avenue"
	user_question = "Bonjour, ou se trouve la Tour Eiffel ?"
	short_question = "cool"

	# We test that parser receive a string with user input minimalized
	def test_user_input(self):
		INPUT = script.Parser(self.user_question)
		assert INPUT.user_input == "bonjour, ou se trouve la tour eiffel ?"

	# We test that parser doesn't activate if user input is too short (<5)
	def test_input_lenght(self):
		INPUT = script.Parser(self.short_question)
		assert INPUT.parsed_input == ""

	# We test that punctuation is deleted by parser
	def test_punct(self):
		INPUT = script.Parser(self.punct)
		assert INPUT.parsed_input == ""

	# We test that parser delete apostrophe
	def test_apost(self):
		INPUT = script.Parser(self.apost)
		assert INPUT.parsed_input == 'avenue'

	# We test that parser split the user input and delete punctuation
	def test_parse(self):
		INPUT = script.Parser(self.user_question)
		assert INPUT.parsed_input == 'tour eiffel'




	
