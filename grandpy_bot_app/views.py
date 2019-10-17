from flask import Flask, render_template, request, jsonify
from .parser import Parser

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/question', methods=['GET', 'POST'])
def question():
	if request.method == 'POST':
		question = request.form['question']
		parse_input = Parser(question)
	return question
	# return render_template('index.html')
