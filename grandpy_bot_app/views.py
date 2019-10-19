from flask import Flask, render_template, request, jsonify
from .parser import Parser
from .answer import Place

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/question', methods=['GET', 'POST'])
def question():
	if request.method == 'POST':
		question = request.form['question']

		# We parse user input and return a list with key words
		parse_input = Parser(question)
		parse_input.parse()

		# We use these key words to search for place with Google Map
		place = Place(parse_input.parsed_input)
		data = place.get_gmaps_resp()

	return question
