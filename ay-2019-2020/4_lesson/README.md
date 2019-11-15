# 4th Lesson

## Working with dictionaries

Preliminaries

 * create a folder for exercises of this class
 * create a new python file in that folder

#### Exercise 1

 * in the python file, create an empty dictionary called `data` (i.e. variable assignment)
 * add to `data` the following key, value pairs:
    * `"name": "my_name"` (where `my_name` is your name)
    * `"age": my_age` (where `my_age` is an integer)
    * `"profession": "student"`
 * create a list called `list_courses` including the following items: `"comp-think", "comp-ling", "scholarly-editing", "knowledge-repr"`
 * add to `data` the following key, value pair:
    * `"courses": list_courses` (where `list_courses` is the list you just created)
 * change the value `student` in `digital humanist`
 * print **all keys and values of the dictionary** (not the dictionary itself!)
 * sort the dictionary by key and print _only_ the keys
 * print all the courses that include the word `comp`
 * print a sentence like the following: "`my_name` is a `my_age`-year-old `profession`. Currently, s/he is attending several courses, namely: `list_courses`"

**Question**: how to concat items of a list into a single string? **Answer** Google it, and tell me what is the best solution you found :)


#### Exercise 2
Let's play with a real json file

 * download the file `data.json` from the folder called `4_lesson`
 * move the json file in the folder you have already created in **Exercise 1** (the one including your python file)
 * open `data.json` in Pycharm

Access the json file from the python file

 * import the module `json`
 * open the json file `with open(...) as ...:`
 * transform the json file in a python data structure `got = json.load(...)`
 * what data structure is this?
 * calculate the number of episodes (i.e. the number of dictionaries in the list)
 * print the titles of the episodes that have an IMDB rating greater than '9.0' (NB what datatype is used for the rating in the json file?)
 * print the titles of the episodes that were released in June 2011

**Question**: how do I compare dates? **Tip** Look for `strptime`
