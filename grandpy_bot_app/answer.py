from .config import GM_API
import requests
import json

class Place:

	def __init__(self, parsed_input):
		self.parsed_input = parsed_input
		self.found_result = True
		self.address = ""
		self.name = ""

	def get_gmaps_resp(self):

		key_words = self.parsed_input

		parameters = {'key': GM_API['KEY'],
			 'input': key_words,
			 'inputtype': 'textquery',
			 'language': 'fr',
			 'fields': 'formatted_address,name',
			 'locationbias': 'ipbias'
		}

		resp = requests.get(GM_API['URL'], params=parameters)
		data = json.loads(resp.text)

		if data['status'] == "OK":
			self.address = data['candidates'][0]['formatted_address']
			self.name = data['candidates'][0]['name']
			self.get_gmaps_coord()

		else:
			self.found_result = False

		print(self.address)


	def get_gmaps_coord(self):
		pass
		

