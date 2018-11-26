# 1st Lesson
## Table of Contents
 * [Introduction to Python](#introduction-to-python)
    * [Characteristics](#characteristics)
    * [Domains](#domains)
    * [Syntax](#syntax)
    * [Data types](#data-types)
    * [Output](#output)
    * [Operators](#operators)
    * [Statements](#statements)
    * [Import modules](#import-modules)
 * [Introduction to Jupyter](#introduction-to-jupyter)
 * [Exercise](#exercise)
 * [Links](#links)

## Introduction to Python

[Guido Van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) wrote Python as a hobby programming project back in the late 1980s. He was fond of watching the famous comedy series - The Monty Python's [Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus) - hence, he chose the name Python. 

[Python](https://www.python.org/) is a multipurpose, high-level, object-oriented, interactive, interpreted and extremely user-friendly programming language.

Latest updated version: Python v3.7

### Characteristics
 * **Highly readable** English-like syntax
 * **Reusable and maintainable** Is less to type, do not need to compile
 * **Portable** Is an interpreted language, no need to change the code in different platforms
 * **Built-in libraries** Pre-built and portable set of libraries for lots of purposes
 * **Extensible and embeddable** Interacts with other technologies (e.g., Java, C++)
 * **Object-Oriented (OOP)** correlate small parts of a problem in a complex workflows

### Domains
 * **Web Application Development** Many frameworks (e.g. Django, Flask, CherryPy)
 * **Numeric computing** Faster than other languages (e.g. Javascript) and lots of libraries
 * **Software Prototyping** Easy-to-use interfaces (e.g. video games)

Here below is a summary of all the information you need to know in order to solve the given task.

### Syntax
##### Variables and identifiers
Python does not require you to define the type of variables, just declare them:
~~~~
a = 2
~~~~
There are few keywords that cannot be used for naming variables:

`False class finally is return` 
`None continue for lambda try True def` 
`from nonlocal while and del global` 
`not with as elif if or yield assert` 
`else import pass break except in raise`

Python is case sensitive: 
~~~~
variable != Variable
~~~~

There are few good practises and rules for writing identifiers and variables: 
 * Combine lowercase letters (`a-z`) uppercase letters (`A-Z`), digits (`1-9`) and underscore (`_`) 
 * Use camelCase(`thisIsMyVariable`) or underscore to separate words (`this_is_my_variable`)
 * Can not start with a digit or contain a special symbol (`|£$%@# etc.`)
 * Use names that make sense `count = 10` rather than `c = 10`

##### Punctuation and indentation
There’s no need to add punctuation at the end of lines. 
~~~~
a = 2
b = 3 
~~~~
We can use semicolons whether we want to put multiple statements in a single line:
~~~~
a = 2 ; b = 3 
~~~~
We use indentation to separate code blocks (use tabs or 4 whitespaces)
~~~~
a = 2
if a > 1:
    print(a)
~~~~
Document your code using comments (when relevant):
~~~~
# a comment to describe the variable assignment
a = 2
# a comment to describe the if condition
    if a > 1:
    return a
~~~~

### Data types
##### Number
There are three data types for representing numbers:
 * Integers `a = int(5)`
 * floating point numbers `a = float(5.0)`
 * complex numbers `a = complex(5+2j)`

##### String
~~~~
s = “This is a string”
s2 = str(25)
~~~~
We can slice a string and retrieve a substring in a specific position. Index starts from 0 in Python:
~~~~
>>> s[1]
‘h’
>>> s[1:4]
‘his’
~~~~

##### List
A list is an ordered sequence of items separated by comma inside square brackets:
~~~~
myList = ['three', 'two', 'one']
~~~~
We can slice a list and retrieve an item in a specific position. Index starts from 0 in Python:
~~~~
>>> myList[2]
'one'
~~~~
We can sort the list by using the method `sorted()`
~~~~
>>> myList = sorted(myList)
>>> myList
['one', 'three', 'two']
~~~~
We can add a new item to the end of the list by using the method `append()`
~~~~
>>> myList.append('star')
>>> myList
['one', 'three', 'two', 'star']
~~~~
We can count how many times items appear in a list using the class `Counter()`
~~~~
>>> count = Counter(myList)
>>> count
Counter({'one':1, 'two':1, 'three':1, 'star':1})
~~~~

##### Dictionary
An unordered collection of key-value pairs inside curly braces:
~~~~
myDict = {‘first’: 1 ,’second’: 2 , ‘third’: 3}
~~~~
Keys can be used to retrieve values:
~~~~
>>> myDict[‘third’]
3
~~~~

##### Tuple
Tuples are sequences, like lists, but cannot be changed unlike lists. Tuples use parentheses, whereas lists use square brackets.
~~~~
tup = (1, 2, 3, 4, 5)
~~~~
Values can be accessed with the usual slicing notation.

### Output
We use the print() function to output data:
~~~~
>>> print(myDict[‘third’])
3

>>> print(‘the value is:’, myDict[‘third’])
the value is: 3

>>> x = 2 ; y = 3
>>> print('The value of x is {} and y is {}'.format(x,y))
The value of x is 2 and y is 3
~~~~
### Operators
##### Arithmetic operators
 * `+` Add two operands or unary plus `x + y`
 * `-` Subtract right operand from the left or unary minus `x - y`
 * `*` Multiply two operands `x * y`
 * `/` Divide left operand by the right one (always results into float) `x / y`
 * `%` Modulus - remainder of the division of left operand by the right `x % y` (remainder of x/y)
 * `//` Floor division - division that results into whole number adjusted to the left in the number line `x // y`
 * `**` Exponent - left operand raised to the power of right `x**y` (x to the power y)
##### Comparison operators
 * `>` Greater that - True if left operand is greater than the right `x > y`
 * `<` Less that - True if left operand is less than the right `x < y`
 * `==` Equal to - True if both operands are equal `x == y`
 * `!=` Not equal to - True if operands are not equal `x != y`
 * `>=` Greater than or equal to - True if left operand is greater than or equal to the right `x >= y`
 * `<=` Less than or equal to - True if left operand is less than or equal to the right `x <= y`
##### Logic operators
 * `and` True if both the operands are true `x and y`
 * `or` True if either of the operands is true `x or y`
 * `not` True if operand is false (complements the operand) `not x`
##### Assignment operators
 * `=` e.g., `x = 5` corresponds to `x = 5`
 * `+=` e.g. `x += 5` corresponds to `x = x + 5`
 * `-=` e.g. `x -= 5` corresponds to `x = x - 5`
 * `*=` e.g. `x *= 5` corresponds to `x = x * 5`
 * `/=` e.g. `x /= 5` corresponds to `x = x / 5`
 * `%=` e.g. `x %= 5` corresponds to `x = x % 5`
 * `//=` e.g. `x //= 5` corresponds to `x = x // 5`
 * `**=` e.g. `x **= 5` corresponds to `x = x ** 5`
 * `&=` e.g. `x &= 5` corresponds to `x = x & 5`
 * `|=` e.g. `x |= 5` corresponds to `x = x | 5`
 * `^=` e.g. `x ^= 5` corresponds to `x = x ^ 5`
 * `>>=` e.g. `x >>= 5` corresponds to `x = x >> 5`
 * `<<=` e.g. `x <<= 5` corresponds to `x = x << 5`
##### Identity operators
 * `is` True if the operands are identical (refer to the same object) `x is True`
 * `is not` True if the operands are not identical (do not refer to the same object) `x is not True`
##### Membreship operators
 * `in` True if value/variable is found in the sequence `5 in x`
 * `not in` True if value/variable is not found in the sequence `5 not in x`

### Statements
##### Conditional statement
A decision might be taken only when a specific condition is satisfied.
There are several forms of if-else conditions. the simplest one is:

**if-else**
~~~~
num = 3
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
~~~~

##### For loop
Interating over a sequence (e.g. a list or a dictionary) is useful when working on  datasets.
~~~~
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val
~~~~
### Import modules
Modules (containing Python definitions and statements) can be imported and reused.
~~~~
import csv , urllib.request, urllib.error, urllib.parse , codecs

with open('titles.csv', 'r', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader: 
        print(row['Title'])
~~~~
## Introduction to Jupyter
[TODO]

## Exercise
Work on a [bibliography](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/1_lesson/titles.csv) on punk music, released by the British Library as a .csv file .

 * Print all titles sorted in alphabetical order. 
 * Print all the titles of references talking (somehow) about “Sex Pistols”
 * Print all the titles of references published after 2000
 * Count references grouped by language. Print results in the form: `Language : count`

## Links
### Introduction to Python
 * [Python tutorial](https://www.programiz.com/python-programming/) The official Python Tutorial

### Introduction to Jupyter
 * [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/)
 * [Markdown](https://support.zendesk.com/hc/en-us/articles/203691016-Formatting-text-with-Markdown) A quick reference guide for formatting text in Markdown

### References for the exercise
 * [urllib](https://docs.python.org/3/library/urllib.html) A python module to open URLs
 * [csv](https://docs.python.org/2/library/csv.html) A python module to read and write .csv files
 * [Counter](https://docs.python.org/2/library/collections.html#collections.Counter) A class of the module `collections` for counting items of a collection
 * [csv file](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/1_lesson/titles.csv) original data is available at [British National Bibliography > Data Services](http://www.bl.uk/bibliographic/download.html#csvpunk)
 * [Chicago Style Manual](http://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-1.html) see *Bibliography entries (in alphabetical order)* for a reference