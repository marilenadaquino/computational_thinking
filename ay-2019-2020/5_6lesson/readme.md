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
Tuples are sequences, like lists. The difference between tuples and lists is that **tuples cannot be changed**. Moreover, tuples use **parentheses**, whereas lists use square brackets.

~~~~
>>> myTup = ('Silvio', 'is')
~~~~

To access values of a tuple we use the usual **slicing notation**

~~~~
>>> myTup[0]
'Silvio'
~~~~

N.B. Since a tuple is immutable you cannot add new elements. You can take chunks of existing tuples and merge them in new ones.

~~~~
>>> myTup2 = ('very','old')
>>> myNewTup = myTup + myTup2
>>> myNewTup
('Silvio', 'is', 'very', 'old')
~~~~

To iterate over a tuple, we use the usual `for` loop.

~~~~
>>> for w in myNewTup:
>>>     print(w)
~~~~

Tuples can be elements of other iterables (data structures). For instance, look at the following **list of tuples**

~~~~
>>> city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
~~~~

We can:

 1. iterate **over tuples** as they are items of a list (by declaring only one variable in the `for` loop for each tuple, which are treated as items -- blackboxes -- inside the list).

 ~~~~
 >>> city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
 >>> for couple in city_list:
 >>>     print('city: ',couple[1])
 city:  Austin
 city:  Houston
 city:  Albany
 city:  Syracuse
 ...
 ~~~~

 2. iterate **over each item of tuples** by declaring bespoke variables for them in the `for` loop, e.g. `state` and `city`. N.B. In order to do it without ùPython throwing an error, **you must know** the number of items included in each tuple.

 ~~~~
 >>> for state, city in city_list:
 >>>     print('country: ', state)
 country:  TX
 country:  TX
 country:  NY
 ...
 ~~~~

### Defaultdict

A `defaultdict` works exactly like a dictionary, but it is initialized with a function (“default factory”) that provides the default value for a non-existing key.

Values of key-value pairs of a dictionary can be anything, such as integers, strings, or other iterables (e.g. lists, tuples, other dictionaries). When we want to **create a new dictionary where values are iterables**, the value we can use `defaultdict` to initialize the first time a given key is used regardless the number of items that will populate the value.

_**Benefit**: A defaultdict will never raises a KeyError. Any key that does not exist gets the value returned by default._

For instance, take the list of tuples wherein the first item is always the name of a country and the second value is always the name of a city falling within that country. We want to create a dictionary out of it where keys are unique values of states, and values are lists of all the cities that fall into a state.


We can initialise an empty default dictionary, called `cities_by_state`, declaring that for each country we want a key associated to the list of cities falling within the country. That is, _for each key we want the value to be a list that may include [0-n] elements_.

~~~~
from collections import defaultdict

>>> city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
>>> cities_by_state = defaultdict(list)
>>> for state, city in city_list:
>>>     cities_by_state[state].append(city)
>>> cities_by_state
~~~~

 1. We import `defaultdict` from `collections`, a python module (no need to download).
 2. we initialize an empty dictionary where values are (by default) lists.
 3. we iterate over the list of tuples `city_list` by declaring two variables (`state` and `city`), i.e. one for each item of the tuple.
 4. we fill the empty dictionary. Notice that rather than using the usual assignment `dict['key_name'] = 'value'` we append the values we want to an empty list, which is defined as the default value of any key in our dictionary.

In detail:

 * the key is defined by the variable `state`
 * the value is a list. To call the value of a dictionary we use the syntax `dict['key']`, that is `cities_by_state[state]` (N.B. the name of the key is a variable!)
 * to fill the lists we use `append`

### Tips and tricks: pretty print
Printing long data structures in python is messy. We can use the `pprint` module and specify some indentation rule for the sake of double-checking our results.
~~~~
>>> import pprint

>>> pp = pprint.PrettyPrinter(indent=2)
>>> pp.pprint(cities_by_state)

defaultdict(<class 'list'>,
{ 'CA': ['Sacramento', 'Palo Alto'],
  'GA': ['Atlanta'],
  'NY': ['Albany', 'Syracuse', 'Buffalo', 'Rochester'],
  'TX': ['Austin', 'Houston', 'Dallas']})
~~~~

### csv.DictReader

We have already seen that the python module `csv` allows us to access a `.csv` file and transform every row in a list.

For instance:

~~~~
import csv

with open('topics.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: # access each row / list of the file
        print(row[0])
~~~~

However, the same module offers another method, called `DictReader`, that allows us to access a `.csv` file and transform every row in a dictionary.

For instance:

~~~~
import csv

with open('topics.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Title'])
~~~~

N.B. This time we have the **headers** in the file. So doing, we can query specific values in rows by just calling the name of the column.

## Exercise

#### Premise: [Dewey Decimal classification](https://en.wikipedia.org/wiki/Dewey_Decimal_Classification)
The DDC is the most widely used librarian classification system in the world. Libraries in more than 135 countries use the DDC to organize and provide access to their collections, and DDC numbers are featured in the national bibliographies of more than 60 countries.

The DDC is a **hierarchy of codes** (a thesaurus) identifying topics. Topics are categories that are used to classify books and other bibliographic resources for accessing them. For instance:

~~~~
700-799 Arts
  Architecture (720)
  painting (750)
  photography (770)
  music (780)
  sport (796)
~~~~

#### Exercise 1: Reconstruct the Dewey classification from a csv file

Look at the list of bibliographic resources related to Harry Potter available at the British Library (file `topics.csv`). These include music scores, books, and web resources.

###### Exercise 1.1
Build and print a **default dictionary** like in the following example:

 ~~~~
 {
     Dewey_number1: [(Type_of_topic1 , Topic1) ,
                     (Type_of_topic1 , Topic1) ,
                     (Type_of_topic1 , Topic2) ,
                     (Type_of_topic2 , Topic2) , ...],
     Dewey_number1: [(Type_of_topic1 , Topic1) ,
                     (Type_of_topic2 , Topic1) ,
                     (Type_of_topic1 , Topic2) ,
                     (Type_of_topic2 , Topic2) , ...]
     ...
 }
 ~~~~

That is, you have to extract **for every row** of the csv file:

 * the Dewey classification numbers, column `Dewey classification`
 * the types of topics that appear along with a DDC number, column `Type of topic`
 * the specific topics belonging to the aforementioned types, column `Topic`.
 * create a defaultdict where keys are unique `Dewey classification` numbers and values are lists of tuples
 * tuples include `Type of topic` and `Topic` that appear together in every row.

_**Problems to solve by your own**: how to append tuples to a list? how to remove duplicate tuples (e.g. `(Type_of_topic1 , Topic1)` appears twice in `Dewey_number1`)_

###### Exercise 1.2

 * create a new default dictionary `cleanDict = defaultdict(dict)`
 * iterate over the dictionary you created in the prior exercise
 * group topics by `Type of topic` and fill in the dictionary in the following form.

~~~~
{
     Dewey_number1: {
        Type_of_topic1 : [Topic1 , Topic2],
        Type_of_topic2 : [Topic2],
     ...}

     Dewey_number2: {
        Type_of_topic1 : [Topic1 , Topic2],
        Type_of_topic2 : [Topic2],
     ...}
 }
~~~~

_**Problems to solve by your own**: how to add items to a list *only if* these are not there yet?_

###### Exercise 1.3

 * print a bullet list like the following one:

~~~~
 - Dewey_number1:
    - Type_of_topic1:
        - Topic1
        - Topic2
    - Type_of_topic2:
        - Topic2
 - Dewey_number2:
    - Type_of_topic1:
      - Topic3
      - Topic4
 ...
~~~~

#### Exercise 2: Reproduce the British Library physical organization
There are several sections at the BL, such as: notated music, Language text, online resources.

###### Exercise 2.1

Print a bullet list like the following one:

 ~~~~
 - Notated music:
    - 013372965
    ...
 ~~~~

 The bullet list includes the following elements:

 * `Content type` the main group
 * `BL record ID` the **ordered list** of British Library IDs that fall within the the group


###### Exercise 2.2

Create a function called `rebuild_bl` that:

 * accepts as parameter the name of the csv file
 * returns the two aforementioned bullet lists (exercise 1.3 and 2.1)

## Links
 * [DDC Classification](https://www.oclc.org/en/dewey/features/summaries.html)
