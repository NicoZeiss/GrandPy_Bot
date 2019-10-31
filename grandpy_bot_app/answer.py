from .config import GM_URL, GM_KEY, GM_PARAMS, WIKI_URL, WIKI_PARAMS, WIKI_LINK, MESSAGES
import requests
import json

class Place:

	def __init__(self, parsed_input):
		self.parsed_input = parsed_input
		self.error = 0

		# GM datas
		self.gmap_datas = ""
		self.address_message = ""

		# Wiki datas
		self.wiki_datas = ""
		self.wiki_message = ""

		# Error message
		self.err_mess = ""
		
		self.filter()

	def filter(self):
		if self.parsed_input != "":
			self.get_gmaps_resp()
			if self.error == 0:
				self.get_wiki_info()
		else:
			self.error = 1
		self.message()

	def get_gmaps_resp(self):

		key_words = self.parsed_input

		parameters = GM_PARAMS
		parameters['key'] = GM_KEY
		parameters['input'] = key_words

		resp = requests.get(GM_URL, params=parameters)
		data = json.loads(resp.text)

		if data['status'] == "OK":
			address = data['candidates'][0]['formatted_address']
			name = data['candidates'][0]['name']
			lat = str(round(data['candidates'][0]['geometry']['location']['lat'],6))
			lng = str(round(data['candidates'][0]['geometry']['location']['lng'],6))
			self.gmap_datas = {"address": address, "name": name, "lat": lat, "lng": lng}

		else:
			self.error = 2


	def get_wiki_info(self):

		parameters = WIKI_PARAMS
		parameters['gsrsearch'] = self.gmap_datas["name"]

		resp = requests.get(WIKI_URL, params=parameters)
		resp_json = json.loads(resp.text)

		page_id = resp_json['query']['pageids'][0]
		extract = resp_json['query']['pages'][page_id]['extract'].replace('\n', ' ')
		link = WIKI_LINK + page_id

		self.wiki_datas = {"page_id": page_id, "extract": extract, "link": link}


	def message(self):
		if self.error == 0:
			self.address_message = MESSAGES["resp_address"]["1"] + " " + self.gmap_datas["address"]
			self.wiki_message = MESSAGES["resp_info"]["1"] + " " + self.wiki_datas["extract"]

		elif self.error == 1:
			self.err_mess = MESSAGES["err_input"]["1"]

		elif self.error == 2:
			self.err_mess = MESSAGES['err_place']["1"]

