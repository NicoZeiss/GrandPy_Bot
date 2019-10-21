#!/usr/bin/python3
# -*- coding: Utf-8 -*-

from flask import Flask
import grandpy_bot_app.answer as script
import pytest


class TestPlace:
	parsed_input = "tour eiffel"
	bad_input = ""

	# We test that user request return one adress, one name, lat and long with GPlace API
	def test_gmap_resp(self):
		PLACE = script.Place(self.parsed_input)
		PLACE.get_gmaps_resp()
		assert PLACE.address == "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France"
		assert PLACE.name == "Tour Eiffel"
		assert PLACE.lat == "48.85837"
		assert PLACE.lng == "2.294481"
		assert PLACE.found_place == True
		assert PLACE.found_coords == True

	# We test that GPlace API return an error if it can't find any result
	def test_error_gmap_resp(self):
		PLACE = script.Place(self.bad_input)
		PLACE.get_gmaps_resp()
		assert PLACE.found_place == False





