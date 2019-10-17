import string
from .config import stop_words, _stop_words

class Parser:

	STOP_WORDS = stop_words
	_STOP_WORDS = _stop_words

	def __init__(self, u_input):
		# Making only one list of stop words
		self.stop = []
		self.stop.extend(self.STOP_WORDS)
		self.stop.extend(self._STOP_WORDS)

		# Lowering user input
		self.user_input = u_input.lower()
		self.parsed_input = []

	def parse(self):
		# We delete punctuation
		str_without_punc = self.user_input.translate(str.maketrans('', '', string.punctuation))
		# We split the question into words list
		self.split_input = str_without_punc.split()

		# We test if some words are in stop words list
		for word in self.split_input:
			if word not in self.stop:
				self.parsed_input.append(word)
