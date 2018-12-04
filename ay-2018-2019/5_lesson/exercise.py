import nltk , nltk.data , collections, string , sys
from nltk.text import Text 
from nltk.probability import FreqDist , ConditionalFreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import *

with open('military.txt') as my_dataFile:
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
	# instantiate the class Text for extracting statistics
	tokens_to_be_analysed = Text(clean_token_text)
	term = 'band'
	print('## total number of words:', len(tokens_to_be_analysed), '\n') 
	print('## lexical diversity:', len(set(tokens_to_be_analysed)) / len(tokens_to_be_analysed), '\n')
	print('## occurrences of the term "', term, '": ', tokens_to_be_analysed.count(term), '\n')
	print('## percentage on the total amount of words:', 100 * tokens_to_be_analysed.count(str(term)) / len(tokens_to_be_analysed))
	print('\n## concordance of the term '+term+':') 
	tokens_to_be_analysed.concordance(term, 75, sys.maxsize)
	print('\n## similar words in the same context of "'+term+'":') 
	tokens_to_be_analysed.similar(term)

	# distribution of words in the cleaned corpus
	print('## frequency distribution of the 100 most common words (without stopwords and punctuation):')
	fd = FreqDist(tokens_to_be_analysed)
	for w,f in fd.most_common(100):
		print(w,':',f)
	# compute frequency distribution for all the bigrams in the text
	bgs = nltk.bigrams(tokens_to_be_analysed)
	fdist = FreqDist(bgs)
	print('\n## distribution of 50 most common bigrams:\n', fdist.most_common(50),'\n')

	# Collocation of bigrams that appear more than twice
	bigram_measures = nltk.collocations.BigramAssocMeasures()
	finder = BigramCollocationFinder.from_words(tokens_to_be_analysed)
	finder.apply_freq_filter(2) # filter bigrams that appear more than 3 times
	scored = finder.score_ngrams(bigram_measures.raw_freq) # score bigrams by their frequency (raw freq)
	print("\n## collocation of words that appear more than twice:\n", scored)
    
	# rating bigrams that will likely occour
	scored2 = finder.score_ngrams(bigram_measures.likelihood_ratio) # score bigrams by their likelihood
	print("\n## collocation of words that are likely to appear together:\n",scored2)