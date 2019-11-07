# 4th Lesson
## Table of Contents
 * [Dictionaries! Dictionaries! Dictionaries!](#dictionaries)
 * [JSON and Lists of Dictionaries](#JSON_and_Lists_of_Dictionaries)
 * [Exercises](#exercises)

## Dictionaries
A sictionary is an *unordered* collection of items. An item of dictionary has a `key: value` pair.

### Create a dictionary
Initialise an empty dictionary:
~~~~
my_dict = {}
~~~~
or
~~~~
my_dict = dict()
~~~~

Keys must be of immutable type (string, number or tuple with immutable elements) and must be unique. Values can change.
~~~~
my_dict = {'fruit1': 'apple', 'fruit2': 'orange'}
~~~~

### Modify a dictionary
Dictionary are mutable. Add new pairs using assignment operator.
~~~~
>>> my_dict['fruit3'] = 'bananas'
>>> print(my_dict)
{'fruit2': 'orange', 'fruit3': 'bananas', 'fruit1': 'apple'}
~~~~

Update the value of existing values.

~~~~
>>> my_dict['fruit3'] = 'banana'
>>> print(my_dict)
{'fruit2': 'orange', 'fruit3': 'banana', 'fruit1': 'apple'}
~~~~

You can add more than one pair at time. For instance:

~~~~
>>> another_dict = {}
>>> yet_another_list = ['apple','orange','strawberry','pineapple','blueberry']
>>> n = 0
>>> for fruit in yet_another_list:
>>> 	n += 1
>>> 	another_dict['fruit'+str(n)] = fruit
>>> print(another_dict)
{'fruit2': 'orange', 'fruit4': 'pineapple', 'fruit5': 'blueberry', 'fruit1': 'apple', 'fruit3': 'strawberry'}
~~~~

### Access a dictionary
Dictionaries are optimized to retrieve values when the key is known. To get the value of a specified key:

~~~~
>>> print(my_dict['fruit1'])
apple
~~~~

When keys are unknown, iterate over all key/value pairs:

~~~~
>>> for k,v in another_dict.items():
>>> 	print(k, ' has value ', v)
fruit1  has value  apple
fruit5  has value  blueberry
fruit4  has value  pineapple
fruit2  has value  orange
fruit3  has value  strawberry
~~~~

We can access only keys or only values as well.

~~~~
>>> for k in another_dict.keys():
>>> 	print(k)
fruit4
fruit1
fruit5
fruit3
fruit2

>>> for k in another_dict.values():
>>> 	print(k)
pineapple
apple
blueberry
strawberry
orange
~~~~

What if the value of a pair is a list (or another iterable)? We use both the key of the pair and the index of the list item we want to access. For instance:

~~~~
>>> dictionary_with_list = {'fruit': 'apple', 'smallfruits': ['strawberry','blueberry']}
>>> print('example 9\n', dictionary_with_list['smallfruits'][0])
strawberry
~~~~

We can build lists of dictionaries. Dictionaries can be accessed as list item, and then its values by means of the key.

~~~~
>>> list_of_dictionaries = [{'fruit1': 'apple','fruit2': 'orange'},{'fruit3': 'banana', 'fruit4': 'pineapple'}]
>>> for fruitDict in list_of_dictionaries:
>>> 	print(fruitDict['fruit2'])
orange
~~~~

### Sorting

We can sort any iterable with `sorted()`.

~~~~
>>> for k,v in sorted(another_dict.items()):
>>> 	print(k, ' has value ', v)
fruit1  has value  apple
fruit2  has value  orange
fruit3  has value  strawberry
fruit4  has value  pineapple
fruit5  has value  blueberry
~~~~

The dictionary is sorted by key. Sorting by value is tricky and there are plenty of ways to do it - is up to you to find your own way :).

## JSON and Lists of Dictionaries

JSON is a data format (a string) very similar to a Python dictionary, that is a data structure (in-memory object). Likewise .csv files. JSON files (.json) can store data, and can be *serialised* as Python dictionaries.

~~~~
import json
with open('my_file.json', encoding='utf-8') as my_list_of_dictionaries:
   data = json.load(my_list_of_dictionaries)
~~~~

## Exercises

Open the file `ArtistsMoMA.json` and explore it.

 * Print all the artists' names.
 * Print the names of Italian artists.
 * Print the names of Italian artists born after 1923.
 * Print the names of female artists born after 1923.
 * Create a new dictionary including names and birth dates of female artists born after 1900. Print all the birth dates included in the new dictionary.
 * Create a new list of dictionaries including all the dictionaries describing female artists that during the WWII were in their twenties.
