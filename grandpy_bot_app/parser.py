import string

class Parser:

	def __init__(self, u_input):
		self.user_input = u_input

	def parse(self):
		str_without_punc = self.user_input.translate(str.maketrans('', '', string.punctuation))
		self.split_input = str_without_punc.split()

