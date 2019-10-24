from .config import GM_URL, GM_KEY, GM_PARAMS, WIKI_URL, WIKI_PARAMS, WIKI_LINK, MESSAGES
import requests
import json

class Place:

	def __init__(self, parsed_input):
		self.parsed_input = parsed_input
		self.error = 0

		# GM datas
		self.address = ""
		self.name = ""
		self.lat = ""
		self.lng = ""

		# Wiki datas
		self.page_id = ""
		self.extract = ""
		self.link = ""

		# Messages
		self.address_mess = ""
		self.info_mess = ""
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
			self.address = data['candidates'][0]['formatted_address']
			self.name = data['candidates'][0]['name']
			self.lat = str(round(data['candidates'][0]['geometry']['location']['lat'],6))
			self.lng = str(round(data['candidates'][0]['geometry']['location']['lng'],6))

		else:
			self.error = 2


	def get_wiki_info(self):

		parameters = WIKI_PARAMS
		parameters['gsrsearch'] = self.name

		resp = requests.get(WIKI_URL, params=parameters)
		resp_json = json.loads(resp.text)
		
		try:
			self.page_id = resp_json['query']['pageids'][0]
			self.extract = resp_json['query']['pages'][self.page_id]['extract'].replace('\n', ' ')
			self.link = WIKI_LINK + self.page_id

		except KeyError:
			self.error = 3

	def message(self):
		if self.error == 0:
			self.address_mess = MESSAGES["resp_address"]["1"] + " " + self.address
			self.info_mess = MESSAGES["resp_info"]["1"] + " " + self.extract

		elif self.error == 1:
			self.err_mess = MESSAGES["err_input"]["1"]

		elif self.error == 2:
			self.err_mess = MESSAGES['err_place']["1"]

		elif self.error == 3:
			self.err_mess = MESSAGES['err_wiki']["1"]

