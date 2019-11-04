from flask import Flask, render_template, request, jsonify
from .config import GM_KEY
from .parser import Parser
from .answer import Place

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', GmApiKey = GM_KEY)


@app.route('/question', methods=['POST'])
def question():

	question = request.form['user_input']

	# We parse user input and return a list with key words
	parse_input = Parser(question)

	# We use these key words to search for place with Google Map
	place = Place(parse_input.parsed_input)

	return jsonify(
		gmap_datas=place.gmap_datas,
		wiki_message=place.wiki_message,
		address_message=place.address_message,
		error_message=place.err_mess,
		error=place.error
		)

