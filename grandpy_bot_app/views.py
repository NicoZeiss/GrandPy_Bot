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
		lat=place.lat,
		lng=place.lng,
		name=place.name,
		addresse=place.address_mess,
		wikinfo=place.info_mess,
		error=place.err_mess
		)

