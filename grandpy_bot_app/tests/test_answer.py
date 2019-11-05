#!/usr/bin/python3
# -*- coding: Utf-8 -*-

import grandpy_bot_app.answer as script
import requests


class TestPlace:
    parsed_input = "tour eiffel"
    wrong_input = "dsgrdeyh"
    short_input = ""

    # We test that too short input generate an error
    def test_short_input(self):
        PLACE = script.Place(self.short_input)
        assert PLACE.error == 1

    # We test that GPlace API return an error if it can't find any result
    def test_error_gmap_resp(self):
        PLACE = script.Place(self.wrong_input)
        assert PLACE.error == 2

    # We test the returned messages with a right input
    def test_messages(self):
        PLACE = script.Place(self.parsed_input)
        assert PLACE.address_message == "Ton PaPy sait tout ! Voici l'adresse que tu désires : Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France"
        assert PLACE.wiki_message == "Et en bonus, je peux même t'en dire un peu plus, ça ne te coûtera pas un denier de plus ! La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs. D’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans."
        assert PLACE.err_mess == ""

    # We test that app return an error when input is too short
    def test_err_mess1(self):
        PLACE = script.Place(self.short_input)
        assert PLACE.err_mess == "Moi pas comprendre toi ! Toi être plus précis avec moi !"

    # We test that app return an error when GMaps can't find any result
    def test_err_mess2(self):
        PLACE = script.Place(self.wrong_input)
        assert PLACE.err_mess == "Désolé bel internaute, mais il va falloir être un peu plus concis, je ne trouve pas le lieu auquel tu fais référence !"


def test_api_return_with_mock(monkeypatch):
    """We create a mock to test each API used"""

    result_gmap = '{"candidates" : [{"formatted_address" : "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France","geometry" : {"location" : {"lat" : 48.85837009999999,"lng" : 2.2944813},"viewport" : {"northeast" : {"lat" : 48.85974697989273,"lng" : 2.29610765},"southwest" : {"lat" : 48.85704732010728,"lng" : 2.29251745}\n            }\n         },\n         "name" : "Tour Eiffel"\n      }\n   ],\n   "status" : "OK"\n}\n'
    result_wiki = '{"batchcomplete":"","continue":{"gsroffset":1,"continue":"gsroffset||"},"query":{"pageids":["1359783"],"pages":{"1359783":{"pageid":1359783,"ns":0,"title":"Tour Eiffel","index":1,"extract":"La tour Eiffel  est une tour de fer puddl\\u00e9 de 324 m\\u00e8tres de hauteur (avec antennes) situ\\u00e9e \\u00e0 Paris, \\u00e0 l\\u2019extr\\u00e9mit\\u00e9 nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l\\u2019Exposition universelle de Paris de 1889, et initialement nomm\\u00e9e \\u00ab tour de 300 m\\u00e8tres \\u00bb, ce monument est devenu le symbole de la capitale fran\\u00e7aise, et un site touristique de premier plan : il s\\u2019agit du troisi\\u00e8me site culturel fran\\u00e7ais payant le plus visit\\u00e9 en 2015, avec 6,9 millions de visiteurs, en 2011 la cath\\u00e9drale Notre-Dame de Paris \\u00e9tait en t\\u00eate des monuments \\u00e0 l\'acc\\u00e8s libre avec 13,6 millions de visiteurs estim\\u00e9s mais il reste le monument payant le plus visit\\u00e9 au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs.\\nD\\u2019une hauteur de 312 m\\u00e8tres \\u00e0 l\\u2019origine, la tour Eiffel est rest\\u00e9e le monument le plus \\u00e9lev\\u00e9 du monde pendant quarante ans."}}}}'

    def mock_api(url, params):

        class Response:
            def __init__(self, resp):
                self.text = resp

        if url == "https://fr.wikipedia.org/w/api.php":
            response = Response(result_wiki)
        if url == "https://maps.googleapis.com/maps/api/place/findplacefromtext/json":
            response = Response(result_gmap)

        return response

    monkeypatch.setattr(requests, 'get', mock_api)

    place = script.Place("tour eiffel")

    assert place.wiki_datas == {"page_id": "1359783", "extract": "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs. D’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans.", "link": "http://fr.wikipedia.org/?curid=1359783"}
    assert place.gmap_datas == {"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France", "name": "Tour Eiffel", "lat": "48.85837", "lng": "2.294481"}
	