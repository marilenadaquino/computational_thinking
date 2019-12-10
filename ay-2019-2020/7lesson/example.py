import nltk , nltk.data , collections, string , sys
from nltk.text import Text 
from nltk.probability import FreqDist , ConditionalFreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import *

with open('military.txt') as my_dataFile: # open a file and assign it a name
	# open a txt file and transform it in a string
	my_text = my_dataFile.read() 
	# everything in lowercase
	my_text = my_text.lower()  
	# prepare the list of punctuation symbols
	excludedPunct = set(string.punctuation) 
	# prepare the list of stopwords
	stopWordsList = set(stopwords.words('english')) 
	# tokenize the text
	token_text = word_tokenize(my_text) 
	# remove stopwords and punctuation. Create a new list with list comprehension
	clean_token_text = [w for w in token_text if w not in excludedPunct and w not in stopWordsList]
	# count the number of words in the text (stopwords excluded)
	number_of_words=len(clean_token_text)
	print(number_of_words)
	# count the number of unique words in the text
	unique_words_list = set(clean_token_text)
	print(len(unique_words_list))
	# instantiate the class Text for extracting statistics
	tokens_to_be_analysed = Text(clean_token_text)
	term = 'military'
	# explore concordance of a term
	tokens_to_be_analysed.concordance(term, 75, sys.maxsize) # print the concordance of the specified term
	# retrieve terms that appear in the same position
	tokens_to_be_analysed.similar(term)
	# frequency distribution of all words
	fdist = FreqDist() 
	fdist = FreqDist(tokens_to_be_analysed)
	for word,count in fdist.items():
		print(word, 'appears n.', str(count), 'times')
	# frequency distribution of the 10 most common words
	print(fdist.most_common(10))
	# frequency distribution of a specific word
	print(fdist.freq('band')) 
	# frequency distribution of all the bigrams
	bgs = nltk.bigrams(tokens_to_be_analysed)
	fdist = nltk.FreqDist(bgs)
	# frequency distribution of the 10 most common bigrams
	print(fdist.most_common(10))
	# collocation of bigrams
	bigram_measures = nltk.collocations.BigramAssocMeasures()
	finder = BigramCollocationFinder.from_words(tokens_to_be_analysed)
	# filter out bigrams that appear less than twice
	finder.apply_freq_filter(2)
	scored = finder.score_ngrams(bigram_measures.raw_freq)
	print(scored)