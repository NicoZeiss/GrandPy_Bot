import json
import requests
from .config import GM_URL, GM_KEY, GM_PARAMS, WIKI_URL, WIKI_PARAMS, WIKI_LINK, MESSAGES


class Place:
    """
    Here is the main class which will permit to :
        - extract coords and address from GMAPS API
        - extract wiki datas from wiki API
        - create answers to send to frontend
    """

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
        """We check parser and API results to let app now if it has to raise an error"""

        if self.parsed_input != "":
            self.get_gmaps_resp()
            if self.error == 0:
                self.get_wiki_info()
        else:
            self.error = 1
        self.message()


    def get_gmaps_resp(self):
        """This method extracts address and coords from GMPS API"""

        key_words = self.parsed_input

        # set up parameters for the request
        parameters = GM_PARAMS
        parameters['key'] = GM_KEY
        parameters['input'] = key_words

        # we request the API and save results into var
        resp = requests.get(GM_URL, params=parameters)
        data = json.loads(resp.text)

        # Important datas are saved into an array (if response's statut is OK)
        if data['status'] == "OK":
            address = data['candidates'][0]['formatted_address']
            name = data['candidates'][0]['name']
            lat = str(round(data['candidates'][0]['geometry']['location']['lat'], 6))
            lng = str(round(data['candidates'][0]['geometry']['location']['lng'], 6))
            self.gmap_datas = {"address": address, "name": name, "lat": lat, "lng": lng}

        else:
            self.error = 2


    def get_wiki_info(self):
        """This method extracts summary about user input thanks to Wiki API"""

        # set up parameters for the request
        parameters = WIKI_PARAMS
        parameters['gsrsearch'] = self.gmap_datas["name"]

        # we request the API and save results into var
        resp = requests.get(WIKI_URL, params=parameters)
        resp_json = json.loads(resp.text)

        # Important datas are saved into an array
        page_id = resp_json['query']['pageids'][0]
        extract = resp_json['query']['pages'][page_id]['extract'].replace('\n', ' ')
        link = WIKI_LINK + page_id
        self.wiki_datas = {"page_id": page_id, "extract": extract, "link": link}


    def message(self):
        """This method create responses that will be sent to frontend app"""

        if self.error == 0:
            self.address_message = MESSAGES["resp_address"]["1"] + " " + self.gmap_datas["address"]
            self.wiki_message = MESSAGES["resp_info"]["1"] + " " + self.wiki_datas["extract"]

        elif self.error == 1:
            self.err_mess = MESSAGES["err_input"]["1"]

        elif self.error == 2:
            self.err_mess = MESSAGES['err_place']["1"]
