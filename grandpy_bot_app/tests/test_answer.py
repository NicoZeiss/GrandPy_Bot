#!/usr/bin/python3
# -*- coding: Utf-8 -*-

from flask import Flask
import grandpy_bot_app.answer as script
import pytest


class TestPlace:
	parsed_input = "tour eiffel"
	bad_input = "dsgrdeyh"
	short_input = ""

	# We test that too short input generate an error
	def test_short_input(self):
		PLACE = script.Place(self.short_input)
		assert PLACE.error == 1
		assert PLACE.lat == ""

	# We test that user request return one adress, one name, lat and long with GPlace API
	def test_gmap_resp(self):
		PLACE = script.Place(self.parsed_input)
		assert PLACE.address == "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France"
		assert PLACE.name == "Tour Eiffel"
		assert PLACE.lat == "48.85837"
		assert PLACE.lng == "2.294481"
		assert PLACE.error == 0

	# We test that GPlace API return an error if it can't find any result
	def test_error_gmap_resp(self):
		PLACE = script.Place(self.bad_input)
		assert PLACE.error == 2





