from .config import GM_URL, GM_KEY, GM_PARAMS, WIKI_URL, WIKI_PARAMS
import requests
import json

class Place:

	def __init__(self, parsed_input):
		self.parsed_input = parsed_input
		self.error = 0
		self.address = ""
		self.name = ""
		self.lat = ""
		self.lng = ""
		
		if self.parsed_input != "":
			self.get_gmaps_resp()
			self.get_wiki_info()
		else:
			self.error = 1


	def get_gmaps_resp(self):

		key_words = self.parsed_input

		parameters = GM_PARAMS
		parameters['key'] = GM_KEY
		parameters['input'] = key_words

		resp = requests.get(GM_URL, params=parameters)
		data = json.loads(resp.text)

		if data['status'] == "OK":
			self.address = data['candidates'][0]['formatted_address']
			self.name = data['candidates'][0]['name']
			self.lat = str(round(data['candidates'][0]['geometry']['location']['lat'],6))
			self.lng = str(round(data['candidates'][0]['geometry']['location']['lng'],6))

		else:
			self.error = 2


