# 5th Lesson
## Table of Contents
 * [More on data types](#more-on-data-types)
 	* [Tuples](#tuples)
 	* [Defaultdict](#defaultdict)
 * [Dewey Decimalclassification](#dewey-decimal-classification)
 * [Exercise](#exercise)
 * [Links](#links)

## More on data types

### Tuples
Tuples are sequences, like lists. The difference between tuples and lists is that tuples cannot be changed unlike lists. Moreover, tuples use parentheses, whereas lists use square brackets.

~~~~
>>> myTup = ('Silvio', 'is')
~~~~
To access values of a tuple we use the usual slicing notation
~~~~
>>> myTup[0]
'Silvio'
~~~~
N.B. Since a tuple is immutable you cannot add new elements. You can take a chunk and merge it with another one.

~~~~
>>> myTup2 = ('very','old')
>>> myNewTup = myTup + myTup2
>>> myNewTup
('Silvio', 'is', 'very', 'old')
~~~~

### Defaultdict
A defaultdict works exactly like a dict, but it is initialized with a function (“default factory”) that provides the default value for a not existing key.

The values in a dictionary can be anything, such as integers and strings. When the values in a dictionary are collections (lists, dicts, etc.), the value (an empty list or dict) must be initialized the first time a given key is used. defaultdict does this.

Benefit: A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

~~~~
from collections import defaultdict
>>> city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
>>> cities_by_state = defaultdict(list)
>>> for state, city in city_list:
>>>		cities_by_state[state].append(city)
>>> cities_by_state
~~~~

## [Dewey Decimal classification](https://en.wikipedia.org/wiki/Dewey_Decimal_Classification)
The DDC is the most widely used classification system in the world. Libraries in more than 135 countries use the DDC to organize and provide access to their collections, and DDC numbers are featured in the national bibliographies of more than 60 countries. 

## Exercise
Work on a [bunch](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/5_lesson/topics.csv) of resources related to Harry Potter.
 * reconstruct the Dewey classification at the British Library: extract all the Dewey classification numbers, types of topics under a Dewey number, and the specific topics belonging to such types. Build a dictionary, e.g. 

 ~~~~
 {
 	 Dewey number1: [(Type_of_topic1 , Topic1) , (Type_of_topic1 , Topic1) , (Type_of_topic1 , Topic2) , (Type_of_topic2 , Topic2) , ...]
 	 ...
 }
 ~~~~

 clean duplicate tuples (e.g. (Type_of_topic1 , Topic1) ) and group topics by each type of topic (i.e. the first item of a new tuple)

 ~~~~
{
 	 Dewey_number1: [
 	 	(Type_of_topic1 , [Topic1 , Topic2]), 
 	 	(Type_of_topic2 , [Topic2]), 
 	 ...]

 	 Dewey_number2: [
 	 	(Type_of_topic1 , [Topic1 , Topic2]), 
 	 	(Type_of_topic2 , [Topic2]), 
 	 ...]

 }
 ~~~~
 
 finally, print a bullet list like the following:
 
 ~~~~
 - Dewey_number1:
 	- Type_of_topic1: 
 		- Topic1 
 		- Topic2
 	- Type_of_topic2: 
 		- Topic2
 ...
 ~~~~

 * reproduce the British Library organization: 
 	* construct three sections: notated music, texts and online resources ('Content type')
 	* for each section provide an ordered list of British Library IDs ('BL record ID')

 ~~~~
 - Notated music:
 	- 013372965
 	...
 ~~~~

## Links
 * [DDC Classification](https://www.oclc.org/en/dewey/features/summaries.html)
 * [data](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/5_lesson/topics.csv)