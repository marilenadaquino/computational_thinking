# 4th Lesson
## Table of Contents
 * [Data reconciliation](#data-reconciliation)
    * [Authority files](#authority-files)
    * [Querying APIs](#querying-apis)
    * [Web scraping](#web-scraping)
    * [Fuzzy String Matching](#fuzzy-string-matching)
    * [Precision and recall](#precision-and-recall)
 * [More on functions](#more-on-functions)
 	* [Try-except](#try-except)
 * [A script for reconciling data against DBPedia](#a-script-for-reconciling-data-against-dbpedia)
 * [Exercise](#exercise)
 * [Links](#links)

## Data reconciliation
Textual data in humanities can be messy, not clean and fuzzy. We may have data that are similar to data belonging to other sources, e.g. data about photographers, but slight differences between strings, due to different naming conventions prevent us to find a perfect match (e.g. 'Yvonne De Rosa', 'Y. De Rosa', 'De Rosa, Y.'). A good practice and a very common task is to reconcile data among data sources, in order to integrate and further process data. 

We'll use a pure-python approach to reconcile our data against an external source, but be aware that there are several technologies more easy-to-use, e.g. [Openrefine](http://openrefine.org/). 

### Authority files
When reconciling data to an external source, the best practice is to refer to an authority file, i.e., a dataset, a vocabulary, or a thesaurus well-known and reused in a large community, that includes all the information required to identify an entity. 

There are several established authority files, e.g. [VIAF](https://viaf.org/) for reconciling data about people, or [geonames](http://www.geonames.org/) for place names. For the sake of simplicity, we'll use [DBPedia](http://wiki.dbpedia.org/), the dataset behind Wikipedia. We'll try fo find matches between names in our data, a local .csv file including names of italian photographers, and any entity we can find in DBPedia, by means of an algorithm for fuzzy string matching.

### Querying APIs
We'll use the [DBPedia lookup Service](http://wiki.dbpedia.org/projects/dbpedia-lookup), which is an [API](https://en.wikipedia.org/wiki/Application_programming_interface) that accepts a keyword in a query string, and returns an XML document including a buch of [metadata](https://en.wikipedia.org/wiki/Metadata) about the entity you searched (if found). 

Among this metadata, there is a URI that identifies the corresponding entity - that's the identifier we are looking for. 

E.g. we want to search "Tina Modotti" in DBPedia, an italian photographer whose name is included in our local file. To perform such a query we build a URI that starts with `http://lookup.dbpedia.org/api/search/KeywordSearch?MaxHits=1&QueryString=` and we add a string parameter in the end, `Tina Modotti` (we do not care about whitespaces, that are handled during the request to the API). The API returns a [XML file](http://lookup.dbpedia.org/api/search/KeywordSearch?MaxHits=1&QueryString=Tina%20Modotti), wherein the element <URI> contains `http://dbpedia.org/resource/Tina_Modotti`. 

To request a URI in Python, we built we use the library `requests`. It allows us to send a HTTP request, to manipulate data on the web and access its content.

~~~~
>>> import requests
>>> baseURL = 'http://lookup.dbpedia.org/api/search/KeywordSearch?MaxHits=1&QueryString='
>>> name = 'Tina Modotti'
>>> url = baseURL+name
>>> response = requests.get(url).content
~~~~

So doing, we find a document about 'Tina Modotti'. This algorithm is not aware of homonymous people. Therefore even if we find a match, we are not sure we are talking about the same person.

### Web scraping
We said that once the query is performed and there is a match, a XML file is returned to the user. In particular, the DBPedia lookup API returns a XML file injected in a HTML file. To access (scrap) contents of a web page we use another module, called `BeautifulSoup`. 

The method *BeautifulSoup* accepts a HTML file as first argument, and a parser as a second argument. Generally, when a HTML file is scraped, we call a *html.parser*. In this case, a XML is returned in the web page, thus we use a parser for XML documents, i.e., *lxml*. 

To navigate the tree of elements we use the method **find()** and we pass the element we want to access. The method **text** retrieved the text included in an element. In this way we scrap the element `<uri></uri>` containing our identifier.

~~~~
>>> from bs4 import BeautifulSoup
>>> record = BeautifulSoup(response, "lxml").find('html').find('body').find('arrayofresult').find('result')
>>> uri = record.find('uri').text
~~~~

### Fuzzy String Matching
As we said, the match we found may be wrong, because of several reason, e.g. homonymous people, bugs in the search API. Thus we go for a double-check between our strings and the label of the entity we found, which in our XML file is included in the element *label*.

~~~~
>>> label = record.find('label').text.encode('utf-8') # we encode the string, since ther might be special characters
~~~~

To compare similar but slightly different strings we use the module `fuzzywuzzy`, which is a library for fuzzy string matching that uses several measures to describe similarities. It compare two strings and returns a percentage representing the quality of the match.

A simple string similarity is measured by the method **ratio**, with a measurement of edit distance (kind of string closeness).
~~~~
>>> from fuzzywuzzy import fuzz
>>> fuzz.ratio('Tina Modotti ', 'Tina Modotti')
96
~~~~

Sometimes there is a significative difference between two strings, but they clearly refer to the same entity (example 1). At the opposite, very similar strings refer to two different entities (example 2).

~~~~
>>> fuzz.ratio("YANKEES", "NEW YORK YANKEES") 
61
>>> fuzz.ratio("NEW YORK METS", "NEW YORK YANKEES") 
75
~~~~

Therefore we look for the "best partial match" between two strings, that is provided by the method **partial_ratio** and we obtain:

~~~~
>>> fuzz.partial_ratio("YANKEES", "NEW YORK YANKEES") 
100
>>> fuzz.partial_ratio("NEW YORK METS", "NEW YORK YANKEES") 
69
~~~~

Another common situation is when two strings contain similar substrings but they are in different order. We use the method **token_sort_ratio** to sort tokens alphabetically and then compare strings. An alternative method is **token_set_ratio** which consider only unique tokens (a set) in the string, regardless the position.

~~~~
>>> fuzz.token_sort_ratio("Tina, Modotti", "Modotti Tina")
100
>>> fuzz.token_set_ratio("Tina Modotti, Modotti", "Tina Modotti")
100
~~~~

Sometimes, none of this measure fits perfectly the situation and it can be useful to measure their average in order to have andother parameter for qualifying the match.

~~~~
avg = (ratio+partialRatio+tokenSort+tokenSet)/4
~~~~

### Precision and recall
In information retrieval, *precision* is a measure that takes into account the relevant instances among the retrieved ones and qualify the algorithm used to retrieve instances. We define *precision* as the number of correct results divided by the number of all returned results.

~~~~
precision = numCorrectResults / numRetrievedResults
~~~~

*Recall* is the fraction of relevant instances over the total amount of possible relevant instances. We define *recall* as the number of correct results divided by the number of results that should have been returned.

~~~~
recall = numCorrectResults / numExpectedResults
~~~~

## More on functions

### Try-except
Till now we have seen how errors are handled by python: a `SyntaxError` is the most common situation, and the interpreter returns a message explaining the error detected. Sometimes errors may be caused by the operations we are performing (i.e., we can execute a code in some cases but not in others). In the latter case we have to handle `exceptions`.

~~~~
>>> (x,y) = (5,0)
>>> try:
>>> 	z = x/y
>>> except:
>>> 	print("error! divide by zero")
~~~~

## A script for reconciling data against DBPedia
This time, instead of writing our code from scratch, we'll adapt an existing [script](https://github.com/ehanson8/viaf-dbpedia-reconciliation-python/blob/master/dbpediaReconciliationGeneral.py) to our purposes.

~~~~
import requests
import csv
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
import urllib

baseURL = 'http://lookup.dbpedia.org/api/search/KeywordSearch?MaxHits=1&QueryString='

f=csv.writer(open('dbpediaResultsGeneral.csv', 'wb'))
f.writerow(['search']+['result']+['description']+['ratio']+['partialRatio']+['tokenSort']+['tokenSet']+['avg']+['uri'])
with open('organizations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = str(row['name'])
        nameEdited = urllib.quote(name.decode('utf-8-sig').encode('utf-8').strip())
        url = baseURL+nameEdited.strip()
        response = requests.get(url).content
        record = BeautifulSoup(response, "lxml").find('html').find('body').find('arrayofresult').find('result')
        try:
            label = record.find('label').text.encode('utf-8')
            uri = record.find('uri').text.encode('utf-8')
            description = record.find('description').text.encode('utf-8')
        except:
            label = ''
            uri = ''
            description = ''
        ratio = fuzz.ratio(name, label)
        partialRatio = fuzz.partial_ratio(name, label)
        tokenSort = fuzz.token_sort_ratio(name, label)
        tokenSet = fuzz.token_set_ratio(name, label)
        avg = (ratio+partialRatio+tokenSort+tokenSet)/4
        f=csv.writer(open('dbpediaResultsGeneral.csv', 'a'))
        f.writerow([name.strip()]+[label]+[description.strip()]+[ratio]+[partialRatio]+[tokenSort]+[tokenSet]+[avg]+[uri])
~~~~

## Exercise
Work on an [authority file of italian photographers](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/4_lesson/Authority-Photographers.csv) and a [script](https://github.com/ehanson8/viaf-dbpedia-reconciliation-python/blob/master/dbpediaReconciliationGeneral.py) for reconciling data against DBPedia.

 * adapt the code to your local .csv file. Print results instead of writing a new file 
 * distinguish names that have a match and names that do not have a match in results
 * what can you say about recall and precision of data retrieved? Test the precision of data reconciled, by looking for the string "photo" in both the elements 'description' and 'Label'. Update the function in order to calculate both recall and precision.
 * add a new field DESCRIPTION in results, and integrate the text from the element of the xml file returned by the lookup API of DBPedia

### References for the exercise
 * [Python script](https://github.com/ehanson8/viaf-dbpedia-reconciliation-python/dbpediaReconciliationGeneral.py) for reconciling data against DBpedia
 * [DBPedia lookup Service](http://wiki.dbpedia.org/projects/dbpedia-lookup)
 * [Requests](http://docs.python-requests.org/en/master/) py library for HTTP requests
 * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) py library for web scraping
 * [FuzzyWuzzy](https://pypi.python.org/pypi/fuzzywuzzy) py library for fuzzy string comparison
 * [csv file](https://raw.githubusercontent.com/marilenadaquino/computational_thinking/master/4_lesson/Authority-Photographers.csv) including a sample of an authority file of photographers