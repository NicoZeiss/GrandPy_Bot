from flask import Flask, render_template, request
from .models import Parser

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

	# if request.method == 'POST':
	# 	user_input = request.form['msg']
	# 	query = Parser(user_input)
	# return render_template('index.html')
