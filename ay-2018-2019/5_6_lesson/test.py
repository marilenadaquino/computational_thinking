import nltk , nltk.data , collections, string , sys
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import *

with open('military.txt') as data_file:
	my_text = data_file.read()
	my_text_lower = my_text.lower()

	token_text = word_tokenize(my_text_lower)

	punct = set(string.punctuation)
	stopwords = set(stopwords.words('english'))
	clean_text = [w for w in token_text if w not in punct and w not in stopwords]

	tokens_to_analyze = Text(clean_text)
	
	term = "military" # define your variable once
	n_military = tokens_to_analyze.count(term)
	total_n_words = len(clean_text) # you forgot to declare total_n_words
	percentage_military = 100 * n_military / total_n_words
	print('\nOCCURRENCES OF TERM:', n_military)
	print('\nPERCENTAGE OF TERM: ',percentage_military)
	print('\nCONCORDANCE OF TERM:')
	tokens_to_analyze.concordance(term, 55, sys.maxsize)
	print('\nSIMILAR WORDS:')
	tokens_to_analyze.similar(term)