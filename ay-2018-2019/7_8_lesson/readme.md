# 7th Lesson
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

If we have a list of tuples, we can (1) iterate over tuples as they are items of a list. By declaring only one variable in the `for` loop each tuple is treated as an item. 
~~~~
>>> city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
>>> for couple in city_list: # declare one variable to define the tuple
>>>     print('city: ',couple[1])
city:  Austin
city:  Houston
city:  Albany
city:  Syracuse
...
~~~~

Otherwise, we can (2) iterate over each item of tuples by declaring bespoke variables for them, e.g. `state` and `city`. 
~~~~
>>> for first, second in city_list: # declare a variable for each item in the tuple
>>>     print('country: ', first)
country:  TX
country:  TX
country:  NY
...
~~~~

### Defaultdict
A defaultdict works exactly like a dictionary, but it is initialized with a function (“default factory”) that provides the default value for a not existing key.

The values in a dictionary can be anything, such as integers and strings. When the values in a dictionary are collections (lists, dicts, etc.), the value (an empty list or dict) must be initialized the first time a given key is used. defaultdict does this.

**Benefit**: A defaultdict will never raises a KeyError. Any key that does not exist gets the value returned by default.

For instance, take a list of tuples wherein the first item is always the name of a country and the second value is always the name of a city falling within that country. We can initialise an empty default dictionary, called `cities_by_state`, declaring that for each country we want a key associated to the list of cities falling within the country. That is: for each key we want the value to be a list that may include [0-n] elements.
~~~~
from collections import defaultdict
>>> city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
>>> cities_by_state = defaultdict(list)
>>> for state, city in city_list:
>>>     cities_by_state[state].append(city)
>>> cities_by_state
~~~~

Notice how we filled the empty dictionary. Rather than using the assignment `dict['key_name'] = value` we know that the value is always a list, hence we append the values we want to an empty list, which is identified by the name of the key. In detail:
 * the key is defined by the variable `state`
 * the value is a list. To call the value of a dictionary we use the syntax  `name_of_dict[name_of_key]`, that is `cities_by_state[state]`
 * to fill the lists iteratively we use `append`

### Tips and tricks: pretty print
Printing long data structures in python is messy. We can use the `pprint` module and specify some indentation rule for the sake of double-checking our results.
~~~~
>>> import pprint
...
>>> pp = pprint.PrettyPrinter(indent=2)
>>> pp.pprint(cities_by_state)
defaultdict(<class 'list'>,
{ 'CA': ['Sacramento', 'Palo Alto'],
  'GA': ['Atlanta'],
  'NY': ['Albany', 'Syracuse', 'Buffalo', 'Rochester'],
  'TX': ['Austin', 'Houston', 'Dallas']})
~~~~

## [Dewey Decimal classification](https://en.wikipedia.org/wiki/Dewey_Decimal_Classification)
The DDC is the most widely used classification system in the world. Libraries in more than 135 countries use the DDC to organize and provide access to their collections, and DDC numbers are featured in the national bibliographies of more than 60 countries. 

## Exercise
Look at the list of bibliographic resources related to Harry Potter preserved at the British Library that are included in `topics.csv`. These include music scores, books and web resources.

#### Reconstruct the Dewey classification

 * `Dewey classification` Extract all the Dewey classification numbers 
 * `Type of topic` Extract all the types of topics that appear along with a DDC number
 * `Topic` Extract all the specific topics belonging to the aforementioned types. 
 * Build a default dictionary like in the following example, e.g. 

 ~~~~
 {
     Dewey_number1: [(Type_of_topic1 , Topic1) , (Type_of_topic1 , Topic1) , (Type_of_topic1 , Topic2) , (Type_of_topic2 , Topic2) , ...]
     ...
 }
 ~~~~
 
**Problems to solve by your own**: 

 * how to append tuples to a list? 
 * how to remove duplicate tuples (e.g. `(Type_of_topic1 , Topic1)`) 

Once you solved the above problems, 
 * create a new default dictionary `cleanDict = defaultdict(dict)`
 * iterate over the prior dictionary 
 * group topics by Type of topic and fill in the dictionary in the following form.
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
**Problems to solve by your own**: 
 * how to add items to a list *only if* these are not included yet?
 
 Finally, 
  * print a bullet list like the following one:
 
 ~~~~
 - Dewey_number1:
    - Type_of_topic1: 
        - Topic1 
        - Topic2
    - Type_of_topic2: 
        - Topic2
 ...
~~~~

#### Reproduce the British Library physical organization
There are several sections at the BL, such as: notated music, Language text, online resources. Print a bullet list including the following elements:
 * `Content type` the main group 
 * `BL record ID` the ordered list of British Library IDs that fall within the the group

The bullet list should look like the following one:
 ~~~~
 - Notated music:
    - 013372965
    ...
 ~~~~

## Links
 * [DDC Classification](https://www.oclc.org/en/dewey/features/summaries.html)