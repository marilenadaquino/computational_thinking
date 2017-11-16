# 2nd Lesson
## Table of Contents
 * [More on data types](#more-on-data-types)
 * [Defining Functions](#defining-functions)
    * [Built-in Functions](#built-in-functions)
    * [List comprehension](#list-comprehension)
    * [Regular expressions (regex)](#regular-expressions-(regex))
 * [Exercise](#exercise)
 * [Links](#links)
## More on data types
### List 
Python slicing notation `sliceable[start:stop:step]` enable us to access parts of data, and search for items in sequences, such as lists.

 * **start** the beginning index of the slice, the first index is 0. If it's negative, it means to start n items from the end.
 * **stop** the ending index of the slice, it does not include the element at this index.
 * **step** the amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.
~~~~
>>> t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
t[start:end] # from start to end-1
t[start:]    # from start, through the rest of the sequence
t[:end]      # from the beginning to end-1
t[:]         # the whole sequence
~~~~

### Set
A set is an unordered collection of unique items (it does not contain duplicates) separated by comma inside curly braces
~~~~
>>> t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
>>> t
[1, 2, 3, 1, 2, 5, 6, 7, 8]
>>> list(set(t))
[1, 2, 3, 5, 6, 7, 8]
~~~~
Since a set is an unordered collection, position is irrelevant and the slice operator does not work.

## Defining Functions
A function is a group of statements that perform a task. Functions are useful to organize a program in small chunks.
~~~~
def greet(name):
	"""This function greets to
	the person passed in as parameter"""
	print("Hello, " + name + ". Good morning!")
~~~~
Once defined a function it can be called with the required parameters
~~~~
>>> greet(‘guys’)
Hello, guys. Good morning!
~~~~
We use `return` to exit a function. It can contain statements that are evaluated and return a value
~~~~
def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		return num
	else:
		return -num
~~~~
*NB. Variables declared inside a function are not available outside.*

### Built-in functions
We have built-in functions (Python) or user defined functions. Here below a list of some built-in functions useful to accomplish your task.
##### enumerate()
Is a built-in function that accepts an *iterable* (a sequence) as argument and returns an enumerate object, i.e., a tuple containing a count and a value from the iterable.
~~~~
>>> seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Autumn'), (3, 'Winter')]
~~~~
##### append()
We have already seen the `append()` method, which appends to the end of a list a new item.
~~~~
myList.append('end') 
~~~~
##### filter()
Creates a list of elements for which a function returns true. It's used to filter sequences (e.g. lists) according to the rule expressed as argument.
~~~~
>>> myList = ['', 'one', 'three', '', 'two']
>>> myList = filter(None, myList)
>>> print(myList)
['one', 'three', 'two']
~~~~
##### len()
Returns the number of items (i.e., the length) of an object (e.g. string, list, dictionary)
~~~~
>>> myList = ['', 'one', 'three', '', 'two']
>>> print(len(myList))
5
~~~~
##### range()
The `range()` function can be used to generate a sequence of numbers. It's arguments are `range(start,stop,step)`. 
~~~~
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~~
##### split()
`split()` returns a list of words in a string. It takes as argument the separator. 
It can be iterated over lists.
~~~~
>>> authors = ['Belsito, Peter ; Davis, Bob', 'Alexandersson, Gunvor ; Lundquist, Lena']
>>> for auth in authors:
>>>    splitList = auth.split(';')
~~~~
Returns a new list for each iterated list item
~~~~
['Belsito, Peter ', ' Davis, Bob'] 
['Alexandersson, Gunvor ', ' Lundquist, Lena']
~~~~
##### join()
`join()` returns a string which is the concatenation of the strings included in an iterable object.
~~~~
>>> for au in splitList:
>>>     auth = ';'.join(au for au in splitList)
~~~~
Returns the original list
~~~~
['Belsito, Peter ; Davis, Bob']
['Alexandersson, Gunvor ; Lundquist, Lena']
~~~~
##### replace()
`replace()` returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
~~~~
>>> s = 'this is an example'
>>> print(s.replace('is','was'))
'thwas was an example'
~~~~
##### zip()
`zip()` aggregates items from multiple iterable objects
~~~~
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
~~~~
##### del
`del` is a method that removes an item from a list given its index instead of its value.
~~~~
>>> authors = ['Belsito, Peter ; Davis, Bob', 'Alexandersson, Gunvor ; Lundquist, Lena']
>>> del authors[1]
['Belsito, Peter ; Davis, Bob']
~~~~
### List comprehension
List comprehensions provide a concise way to create lists.
~~~~
old_list = ['Gibbon, Peter [person]', 'Centret for udviklingsforskning (Denmark) [organisation]']
new_list = []
for i in old_list:
    if 'organisation' not in i:
        new_list.append(i)
~~~~
Can be written also as:
~~~~
new_list = [i for i in old_list if 'organisation' not in i]
~~~~
### Regular expressions (regex)
Both patterns and strings can be searched in strings by using methods included in `re` module
~~~~
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
~~~~
Among the operations, we ca nsubstitute strings or delete them.
~~~~
>>> old_list = ['Gibbon, Peter [person]', 'Centret for udviklingsforskning (Denmark) [organisation]']
>>> for auth in old_list:
>>>   auth = re.sub("\s?[\(\[].*?[\)\]]\s?", "", auth) # remove brackets and content
old_list = ['Gibbon, Peter', 'Centret for udviklingsforskning']
~~~~
## Exercise
Work on a [bibliography](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/1_lesson/titles.csv) on punk music, released by the British Library as a .csv file . Define functions for solving the following problems:
 * Is there any duplicate in the list? Print the list of duplicate ISBN in the form `ISBN: number`
 * Can you delete duplicates from the dictionary?
 * Print references in [Chicago Style](http://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html): 
 e.g. `LastName1, FirstName1, FirstName2 LastName2, and FirstNameN LastNameN. Title. City: Publisher, date.`

### References for the exercise
 * [Built-in functions](https://docs.python.org/3/library/functions.html) in python
 * [Data structures](https://docs.python.org/3/tutorial/datastructures.html) methods to work with lists
 * [String operations](https://docs.python.org/3/library/string.html) in python
 * [Regular expressions](https://docs.python.org/3/library/re.html) in python
 * [urllib](https://docs.python.org/3/library/urllib.html) A python module to open URLs
 * [codecs](https://docs.python.org/3/library/codecs.html) A python module for encoding and decoding (e.g. texts to bytes and viceversa)
 * [csv](https://docs.python.org/2/library/csv.html) A python module to read and write .csv files
 * [csv file](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/1_lesson/titles.csv) original data is available at [British National Bibliography > Data Services](http://www.bl.uk/bibliographic/download.html#csvpunk)
 * [Chicago Style Manual](http://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) see *Bibliography entries (in alphabetical order)* 
