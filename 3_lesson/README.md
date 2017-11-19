# 3rd Lesson
## Table of Contents
 * [Text processing](#text-processing)
    * [NLTK](#nltk)
    * [Creating a collection](#creating-a-collection)
    * [Cleaning texts](#cleaning-texts)
    * [Tokenization](#tokenization)
    * [Statistics](#statistics)
    * [Frequency distribution](#frequency-distribution)
    * [Bigrams](#bigrams)
 * [Exercise](#exercise)
 * [Links](#links)

## Text processing
In order to analyse quantitative and qualitative aspects of texts, we first need to build a corpus. It is a structured set of texts designed according to our purposes and implemented to accomplish some tasks. In the design phase we need to consider:
 * the size of the corpus
 * the balance of sources
 * the representativeness of corpus with regard of topics/features to analyse

We can look for general statistics (e.g. number of words, lexical diversity, occurrences of terms, frequency distribution) and other meaningful features (e.g. Part-Of-Speech tagging), and prediction models (e.g. which words are likely to appear together?).

### NLTK
[Natural Language Toolkit (NLTK)](http://www.nltk.org/) is a python library that simplifies several common tasks in linguistic analysis, thanks to several bespoke functions. 

### Creating a collection
We collect and save all our texts in a single .txt file. The function `read()` returns the entire contents of the file as a single string. Since we rely on a file that is online, we need to decode the file from bytes to strings by means of the function `decode()`, specifying the encoding standard (`utf-8`).

~~~~
>>> import urllib.request, urllib.error, urllib.parse 
>>> response = urllib2.urlopen(fileName) # open .txt file
>>> text = response.read().decode("utf-8") 
~~~~

### Cleaning texts
'Neat' statistics require 'neat' data, which means we need to remove all those characters (e.g. punctuation) and words (articles, prepositions, etc.) that would make less readable or significant our results. 
##### lower()
The built-in function `lower()` returns a string in lowercase.
~~~~
>>> text.lower()
~~~~
##### punctuation
The module `string` provide a string of characters (punctuation) that we can use to remove punctuation from our text. We define it as a set and we compare it to our text.
~~~~
>>> import string
>>> exclude = set(string.punctuation)
~~~~

##### stopwords
NLTK provides a list of lowercase stop words for several languages. We can create a set including all of them.
~~~~
>>> from nltk.corpus import stopwords
>>> stopWords = set(stopwords.words('english'))
>>> print(stopWords)
set([u'all', u'just', u'being', u'over', u'both', u'through', u'yourselves', u'its', u'before', u'o', u'hadn', u'herself', u'll', u'had', u'should', u'to', u'only', u'won', u'under', u'ours', u'has', u'do', u'them', u'his', u'very', u'they', u'not', u'during', u'now', u'him', u'nor', u'd', u'did', u'didn', u'this', u'she', u'each', u'further', u'where', u'few', u'because', u'doing', u'some', ... ])
~~~~
and compare it with the list of words in our texts (see `word_tokenize`), and then clean our texts.

#### Tokenization
Tokenization classify parts of a string to be further processed. It's a necessary step to perform statistics on sentences or words.

##### sent_tokenize()
`sent_tokenize()` knows what punctuation and characters mark the end of a sentence and the beginning of a new sentence, thus it divides the text according to such separators. We'll use it to calculate frequency distribution of words.
~~~~
>>> from nltk.tokenize import sent_tokenize
>>> text = “this’s a sentence. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn.”
>>> sent_tokenize_list = sent_tokenize(text)
>>> sent_tokenize_list
[“this’s a sentence.”, ‘this is sent two.’, ‘is this sent three?’, ‘sent 4 is cool!’, “Now it’s your turn.”]
~~~~
##### word_tokenize()
Similarly to `sent_tokenize()`, `word_tokenize()` splits words in a text.
~~~~
>>> from nltk.tokenize import word_tokenize
>>> word_tokenize(‘Hello World.’)
[‘Hello’, ‘World’, ‘.’]
>>> word_tokenize(“this’s a test”)
[‘this’, “‘s”, ‘a’, ‘test’]
~~~~
### Statistics
We can perform simple statistics to understand the usage of certain words in specific context.
##### Text
The class `Text` is a wrapper around a sequence of simple (string) tokens, which is intended to support initial exploration of texts (e.g. concordance, words in a similar context).
~~~~
>>> from nltk.text import Text 
>>> textList = text.split() # we split our text, return a list
>>> textList = Text(textList) # we transform the list in an object
~~~~
##### concordance()
Given a word, we can see where it appears by using `concordance()`, which includes following and preceding words in results. In order
~~~~
>>> import nltk , sys
>>> from nltk.text import Text 
>>> term = 'military'
>>> textList.concordance(term, 75, sys.maxsize)
Displaying 31 of 31 matches:
chic black velvet caps naval and military uniforms and academic robesmade 
a banda playing a passadoble and military exercises always apparently ende
we heard there also some russian military singers they were six private so
ectioneering we marched with the military band before us stopped before ol
...
~~~~
The accepted arguments are: the term to be searched, its length and the number of lines you want to be shown. In this case we specified `sys.maxsize` as the maximum number of lines.

##### similar()
To explore which words appear in the same position as the term we are investigating, we use `similar()`.
~~~~
>>> textList.similar(term)
combined fife marching their prussian united french
~~~~

### Frequency distribution
A frequency distribution can be defined as a function mapping from each sample to the number of times that sample occurred as an outcome. Frequency distributions are generally constructed by running a number of experiments, and incrementing the count for a sample every time it is an outcome of an experiment.

##### FreqDist()
`FreqDist()` accepts an iterable object of tokens and returns a dictionary including words and their count 
~~~~
>>> from nltk.tokenize import word_tokenize
>>> from nltk.probability import FreqDist
>>> sent = 'This is an an example sentence'
>>> fdist = FreqDist()
>>>	fdist = FreqDist(word.lower() for word in word_tokenize(sent))
>>>	print(fdist.items())
dict_items([('is', 1), ('example', 1), ('this', 1), ('sentence', 1), ('an', 2)])
~~~~

##### freq()
Return the frequency of a given sample. The frequency of a sample is defined as the count of that sample divided by the total number of sample outcomes that have been recorded by this `FreqDist`. Frequency is a number in the range [0, 1].
~~~~
>>> print(fdist.freq('an'))
0.3333333333333333
~~~~
### Bigrams
A bigram is a sequence of two adjacent elements from a string of tokens, such as letters, syllabs or words. We use bigrams to see which pairs of words appear in our text (so as to characterize a listening experience by its are most common bigrams).
~~~~
>>> tokens = word_tokenize(sent)
>>> bgs = nltk.bigrams(tokens)
>>> fdist = nltk.FreqDist(bgs)
>>> print(fdist.most_common(10))
[(('an', 'example'), 1), (('This', 'is'), 1), (('is', 'an'), 1), (('example', 'sentence'), 1), (('an', 'an'), 1)]
~~~~
##### Collocation 
Collocation is expression of multiple words which commonly co-occur. We use `nltk.collocations.BigramAssocMeasures()` to find collocation of bigrams.
The `collocations` package provides collocation finders which by default consider all ngrams in a text as candidate collocations.
~~~~
>>> import nltk
>>> from nltk.collocations import *
>>> bigram_measures = nltk.collocations.BigramAssocMeasures()
>>> finder = BigramCollocationFinder.from_words(tokens)
>>> scored = finder.score_ngrams(bigram_measures.raw_freq)
>>> sorted(bigram for bigram, score in scored)
~~~~
We can also apply filters, e.g. we want this method to return only bigrams that appear more than 2 times.
~~~~
>>> finder.apply_freq_filter(2)
~~~~
[see documentation](http://www.nltk.org/howto/collocations.html)

## Exercise
Work on a bunch of short [texts](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/3_lesson/military.txt) recording listening experiences of military bands, published by the [LED project](led.kmi.open.ac.uk). We want to understand how to recognize a listening experience in a text, and which elements characterize a listening experience of a military band. 

Define a function that print the following statistics:
 * Total number of words
 * Lexical diversity: `numberOfUniqueWords / totalNumberOfWords`
 * Occurrences of the term `military`
 * Percentage of the term `military` with respect to the total amount of words: `100 * occurrencesOfTerm / totalNumberOfWords`
 * Concordance of the term `military`
 * Other words that appear in the same context of `military`
 * Frequency distribution of the 100 most common words
 * Distribution of the 50 most common bigrams
 * Collocation of bigrams that appear more than three times
 * **OPTIONAL** Score pair of words that are most likely to appear together (i.e. the most common), using `likelihood_ratio` (instead of `raw_freq`) as a measure for scoring bigrams
 * Write a short summary on how you would characterize a listening experience. What is missing in this analysis?

### References for the exercise
 * [Natural Language Toolkit](http://www.nltk.org/) python library for text analysis
 * [txt file](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/3_lesson/military.txt) including texts on listening experiences
