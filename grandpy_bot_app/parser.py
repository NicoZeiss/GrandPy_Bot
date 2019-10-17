import string

class Parser:

	def __init__(self, u_input):
		self.user_input = u_input
		self.split_input = []

	def split_words(self):
		str_with_punc = self.user_input
		str_without_punc = str_with_punc.translate(str.maketrans('', '', string.punctuation))
		self.split_input = str_without_punc.split()

