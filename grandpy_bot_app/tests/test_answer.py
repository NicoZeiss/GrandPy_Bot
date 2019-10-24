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

	# We test that Wiki API return a page id, an extract and the wiki link
	def test_wiki_resp(self):
		PLACE = script.Place(self.parsed_input)
		assert PLACE.page_id == "1359783"
		assert PLACE.extract == "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs. D’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans."
		assert PLACE.link == "http://fr.wikipedia.org/?curid=1359783"

	# We test the messages returned with a right input
	def test_messages(self):
		PLACE = script.Place(self.parsed_input)
		assert PLACE.address_mess == "Ton PaPy sait tout ! Voici l'adresse que tu désires : Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France"
		assert PLACE.info_mess == "Et en bonus, je peux même t'en dire un plus, ça ne te coûtera pas un denier de plus ! La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs. D’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans."
		assert PLACE.err_mess == ""

	# We test that app return an error when input is too short
	def test_err_mess1(self):
		PLACE = script.Place(self.short_input)
		assert PLACE.err_mess == "Moi pas comprendre toi ! Toi être plus concis avec moi !"

	



