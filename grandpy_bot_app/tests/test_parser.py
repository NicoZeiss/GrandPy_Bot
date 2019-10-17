from flask import Flask
import grandpy_bot_app.parser as script
import pytest




class TestParser:
	user_question = "Hello, where is Eiffel tower ?"
	INPUT = script.Parser(user_question)

	# We test that parser receive a string with user input
	def test_user_input(self):
		assert self.INPUT.user_input == "Hello, where is Eiffel tower ?"

	# We test that parser split the user input and delete punctuation
	def test_input_split(self):
		self.INPUT.split_words()
		split_input = self.INPUT.split_input
		assert split_input == ['Hello', 'where', 'is', 'Eiffel', 'tower']

	# We test that parser delete punctuation from
