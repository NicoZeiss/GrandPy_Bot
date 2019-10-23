from .config import GM_API, GM_API_KEY
import requests
import json

class Place:

	def __init__(self, parsed_input):
		self.parsed_input = parsed_input
		self.found_place = True
		self.found_coords = True
		self.address = ""
		self.name = ""
		self.lat = ""
		self.lng = ""

	def get_gmaps_resp(self):

		key_words = self.parsed_input

		parameters = {'key': GM_API_KEY,
			 'input': key_words,
			 'inputtype': 'textquery',
			 'language': GM_API['LANGUAGE'],
			 'fields': 'formatted_address,name,geometry',
			 'locationbias': 'ipbias',
		}

		resp = requests.get(GM_API['PLACE_URL'], params=parameters)
		data = json.loads(resp.text)

		if data['status'] == "OK":
			self.address = data['candidates'][0]['formatted_address']
			self.name = data['candidates'][0]['name']
			self.lat = str(round(data['candidates'][0]['geometry']['location']['lat'],6))
			self.lng = str(round(data['candidates'][0]['geometry']['location']['lng'],6))

		else:
			self.found_place = False

		return  {"lat": self.lat, "lng": self.lng}


