# 5th Lesson
## Table of Contents
 * [Corpus analysis](#corpus_analysis)
 * [Install NLTK](#install_nltk)
 * [Text processing](#text-processing)
    * [Open and read a .txt file](#Open_and_read_a_txt_file)
    * [Everything in lowercase](#Everything_in_lowercase)
    * [Tokenization](#tokenization)
    * [Cleansing](#cleansing)
    * [Statistics](#statistics)
        * [Concordance](#concordance)
        * [Similarity](#similarity)
        * [Frequency distribution](#frequency-distribution)
        * [Bigrams](#bigrams)
 * [Exercise](#exercise)
 * [Links](#links)

## Corpus analysis
**Create a corpus**. In order to analyse quantitative and qualitative aspects of texts, we first need to build a corpus. A corpus is a structured set of texts, designed according some purpose and implemented to accomplish some tasks. In the design phase you must consider:
 * the size of the corpus (fit-for-purpose)
 * the balance of sources (different kinds of text)
 * the representativeness of corpus (with regard of topics/features to analyse)

**What is inside a corpus.** It may include plain text (e.g. .txt files), semi-structured texts (e.g. .xml files), or structured data (e.g. .csv files).

**What you can do with corpora (and Python)**. [Natural Language Toolkit (NLTK)](http://www.nltk.org/) is a python library that simplifies several common tasks in linguistic analysis. 
 * statistics (e.g. number of words, lexical diversity, occurrences of single terms, frequency distribution) 
 * extract meaningful features (e.g. Part-Of-Speech tagging, stylometry) 
 * prediction models (e.g. which words are likely to appear together?)

It also includes a number of corpora, grammars, and trained models. Unfortunately, most of them are tailored for english language only.

## Install NLTK
Install NLTK by using `pip install -U nltk` (no matter what is you OS). 

Corpora must be downloaded separately instead. In detail, you create a new pyhon script, called e.g. `install_nltk.py`, copy and paste the following code, and run it. It downloads only the following corpora (it takes a couple of minutes).
~~~~
import nltk 
nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('popular')
~~~~
**NB 1** if you just use `nltk.download()` it will take much longer!
**NB 2** Use the example installation .py file in this folder if you get an SSL error similar to the following one.

~~~~
[nltk_data] Error loading punkt: <urlopen error [SSL: 
[nltk_data] CERTIFICATE_VERIFY_FAILED] certificate verify failed 
[nltk_data] (_ssl.c:646)>
~~~~

## Text processing
'Neat' statistics require 'neat' data, which means we need to perform some actions in order to play with our data properly, namely:
 1. store data somewhere (in our case it will be a .txt file including a bunch of short texts, stored in the same folder of our python file)
 2. lowercase
 2. tokenize (separate) elements your are going to work on (sentences, words, etc.)
 3. clean data to be analysed

### 1. Open and read a .txt file
The method `read()` allows you to open a text file and transform its content in a string.
~~~~
with open('military.txt') as my_dataFile:
	my_text = my_dataFile.read()
~~~~
The variable `my_text` is now a string. Hence, you can manipulate it as you would do with a string.

### 2. Everything in lowercase
If not relevant for the sake of the analysis, we change the text to lowercase, so that if we want to look for specific terms we do not have to worry about its case. The built-in function `lower()` returns a string in lowercase. 

~~~~
>>> my_text = my_text.lower()
~~~~

#### 3. Tokenization
Tokenization implies to split parts of a string to be further processed. It's a necessary step to perform statistics. You can tokenize sentences, with `sent_tokenize()`, or words, with `word_tokenize()`. 

##### word_tokenize()
`word_tokenize()` is a function included in the module `nltk.tokenize`, which splits a text in words. It recognizes linguistic aspects of the string, e.g. punctuation, and splits the text accordingly. It accepts as parameter the string to be tokenized.

The result is a list of words.
~~~~
>>> from nltk.tokenize import word_tokenize
>>> token_text = word_tokenize(my_text)
['the', 'profound', 'impression', 'made', 'upon', 'a', 'crowded', ... ]
~~~~

### 4. Cleansing
Here below are listed some common actions to perform on a corpus of texts before analysing it.

##### Remove punctuation and stopwords
Linguistic analysis mainly encompasses significative parts of a text, such as nouns, verbs, adverbs, and so on. Therefore we should remove all those characters (e.g. punctuation) and words (articles, prepositions, etc.) that would make less readable our text or less significant our results. 

We **prepare the lists of strings** we want to remove from our text. We includes strings we want to remove in lists, so that we can iterate over them in a `for` loop.

The module `string` offers a built-in variable, called `punctuation`, which is a string including all the symbols (i.e., ``!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~``) we want to remove from our text. We transform the string in a `set()`, i.e. a list of unique items, and we assign it a variable name e.g. `excludedTerms`.
~~~~
>>> import string
>>> excludedPunct = set(string.punctuation)
~~~~

NLTK has a module called `corpus`, which includes a number of functions and other modules, such as `stopwords`. We import it with the following syntax.

~~~~
>>> from nltk.corpus import stopwords
~~~~

`stopwords` provides a list called `words` that includes lowercase stop words in several languages. You can specify the language you want as a parameter. Again, we define the list of words as a `set()`.

~~~~
>>> stopWordsList = set(stopwords.words('english'))
>>> print(stopWords)
set([u'all', u'just', u'being', u'over', u'both', u'through', u'yourselves', u'its', u'before', u'o', u'hadn', u'herself', u'll', u'had', u'should', u'to', u'only', u'won', u'under', u'ours', u'has', u'do', u'them', u'his', u'very', u'they', u'not', u'during', u'now', u'him', u'nor', u'd', u'did', u'didn', u'this', u'she', u'each', u'further', u'where', u'few', u'because', u'doing', u'some', ... ])
~~~~

Once we have tokenized our text, we can clean it from punctuation and stopwords. This implies to compare the two lists we created (`excludedPunct` and `stopWordsList`) with the list including all the words of our text (`token_text`). In other terms, we remove terms from the list `token_text` if the same term appears in one of the two other lists.

To remove items from a list we can use the method `remove()`. A possible way to do it is the following:
~~~~
>>> for w in token_text:
>>>		if w in excludedPunct or w in stopWordsList:
>>>			token_text.remove(w)
>>> print(token_text)
['profound', 'impression', 'made', 'upon', 'crowded', 'congregation', 'st.', 'paul', "'s", 'cathedral', ...]
~~~~

#### Tips and tricks: the list comprehension
However, there are smartest ways to do it. Another way, that is actually a shortcut for creating a list as the result of a `for` loop and an `if` statement is the following,
~~~~
clean_token_text = [w for w in token_text if w not in excludedPunct and w not in stopWordsList]
~~~~
This strategy is called `list comprehension`. We assign the value of a new list `= []` as a condition.

### Statistics
We can perform simple statistics to understand the usage of words in context. 

For instance, we can calculate the total number of words in the text (stopwords excluded) and the number of unique words. Since our words are included in a list, the total number of words will be the length of the list itself.
~~~~
>>> number_of_words = len(clean_token_text)
~~~~
To get the number of unique words the list can be transformed in a set (that is a list where there are no duplicates) and the length of the set can be computed.
~~~~
>>> unique_words_list = set(clean_token_text)
>>> number_of_unique_words = len(unique_words_list)
~~~~
The class `Text` is a wrapper around a list of tokens, which is intended to support initial exploration of texts (e.g. concordance, words in a similar context). A class includes several functions that can applied to the object instantiated (i.e., our list of tokens).

~~~~
>>> from nltk.text import Text 
>>> tokens_to_be_analysed = Text(clean_token_text)
~~~~

##### concordance()
Given a word, we can see where it appears by using `concordance()`, which returns the occurrences of the term between following and preceding words. It accepts as parameters:
 * the term to be searched
 * the maximum number of characters to show in each line
 * the maximum number of lines

If you want to visualize the maximum number of lines you must import another built-in module calles `sys` and spwcify `sys.maxsize` as parameter (the largest number supported by the Python). 
~~~~
>>> import sys
>>> term = 'military'
>>> tokens_to_be_analysed.concordance(term, 75, sys.maxsize)
Displaying 31 of 31 matches:
chic black velvet caps naval and military uniforms and academic robesmade 
a banda playing a passadoble and military exercises always apparently ende
we heard there also some russian military singers they were six private so
ectioneering we marched with the military band before us stopped before ol
...
~~~~

##### similar()
`similar()` allows you to explore which words appear in the same position as the term at hand. It accepts as a parameter the term to be searched.
~~~~
>>> tokens_to_be_analysed.similar(term)
combined fife marching their prussian united french
~~~~
**Be aware that** `similar()` is meant to print a string. Hence you do not need to ask to `print()` results.

#### Frequency distribution
Frequency distribution can be defined as a function mapping from each sample to the number of times that sample occurred as an outcome. Frequency distributions are generally constructed by running a number of experiments, and incrementing the count for a sample every time it is an outcome of an experiment.

##### FreqDist()
`FreqDist()` is function included in the module `nltk.probability` which accepts an iterable object of tokens and returns a dictionary including **all the words**  in the given list and their count. It is pretty similar to `Counter()`. 
~~~~
>>> from nltk.probability import FreqDist
>>> sent = 'This is an an example sentence'
>>> fdist = FreqDist()
>>>	fdist = FreqDist(tokens_to_be_analysed)
>>>	for word,count in fdist.items():
>>>		print(word, 'appears n.', str(count), 'times')
near appears n. 1 times
like appears n. 5 times
enveloped appears n. 1 times
...
~~~~
Results are not sorted. To see which are the most common words we use `most_common()`. The method accepts a dictionary obtained by using `FreqDist()` or `Counter()` and returns the list of most frequent words. You can specify the number of results you want to ouptut, e.g. `most_common(10)`, which returns the 10 most common words.
~~~~
>>>	print(fdist.most_common(10))
[('military', 31), ('band', 27), ('music', 19), ('first', 11), ...]
~~~~

##### freq()
Return the frequency of a given word. The frequency of a sample is defined as the count of that sample divided by the total number of sample outcomes that have been recorded by this `FreqDist`. Frequency is a number in the range [0, 1].
~~~~
>>> print(fdist.freq('band'))
0.005291005291005291
~~~~

### Bigrams
A bigram is a sequence of two adjacent elements from a string of tokens, such as letters, syllabs or words. We use bigrams to see which pairs of words appear in our text (so as to characterize the text by its most common bigrams). 

We can calculate the frequency distribution of bigrams as well.
~~~~
>>> bgs = nltk.bigrams(tokens_to_be_analysed)
>>> fdist = nltk.FreqDist(bgs)
>>> print(fdist.most_common(10))
[(('military', 'band'), 14), (('military', 'music'), 3), (('band', 'playing'), 3), ...]
~~~~

##### Collocation 
Collocation is expression of multiple words which commonly co-occur. We use `nltk.collocations.BigramAssocMeasures()` to find collocation of bigrams.
The `collocations` package provides collocation finders which by default consider all ngrams in a text as candidate collocations.

~~~~
>>> from nltk.collocations import *
>>> bigram_measures = nltk.collocations.BigramAssocMeasures()
>>> finder = BigramCollocationFinder.from_words(tokens)
>>> scored = finder.score_ngrams(bigram_measures.raw_freq)
>>> print(scored)
[(('military', 'band'), 0.006734006734006734), (('band', 'playing'), 0.001443001443001443), ....]
~~~~

We can also apply filters, e.g. we want this method to return only bigrams that appear more than 2 times.

~~~~
>>> finder.apply_freq_filter(2)
~~~~
[see documentation](http://www.nltk.org/howto/collocations.html)

## Exercise
Work on a bunch of short [texts](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/3_lesson/military.txt) recording listening experiences of military bands, published by the [LED project](led.kmi.open.ac.uk). We want to understand how to recognize a listening experience in a text, and which elements characterize a listening experience of a military band. 

Print the following statistics:
 * Total number of words
 * Lexical diversity: `numberOfUniqueWords / totalNumberOfWords`
 * Occurrences of the term `military`
 * Percentage of the term `military` with respect to the total amount of words: `100 * occurrencesOfTerm / totalNumberOfWords`
 * Concordance of the term `band`
 * Other words that appear in the same context of `band`
 * Frequency distribution of the 100 most common words. Print " word : frequency"
 * Frequency distribution of the 50 most common bigrams
 * Collocation of bigrams that appear more than twice
 * **OPTIONAL** Score pair of words that are most likely to appear together (i.e. the most common), using `likelihood_ratio` (instead of `raw_freq`) as a measure for scoring bigrams
 * Write a short summary on how you would characterize the text analysed. What do they have in common?

### References for the lesson
 * [Natural Language Toolkit](http://www.nltk.org/) python library for text analysis

### Some guidelines, exercises and more advanced stuff
 * [NLTK python tutorial](https://pythonspot.com/en/tokenizing-words-and-sentences-with-nltk/)
