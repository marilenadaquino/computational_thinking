import csv  
from collections import Counter

# prepare lists including results
listTitles = [] 
sexPistols = []
after2000 = [] 
languages = []

# open a csv file
with open('titles.csv', 'r') as myfile:
	# create a dictionary
    reader = csv.DictReader(myfile)    
    # iterate over rows of the csv file -- over key/value of the dictionary
    for row in reader: 
        listTitles.append(row['Title'])
        if ("sex pistols" in row['Title'].lower() ) or ("sex pistols" in row['Other titles'].lower()) or ("sex pistols" in row['Topics'].lower()):
        	sexPistols.append(row['Title'])
        if int(row["Date of publication"]) >=2000:
        	after2000.append(row["Title"])
        languages.append(row["Languages"])

# print all titles sorted alphabetically
sortedListTitles = sorted(listTitles)
# print(sortedListTitles)
# print(sexPistols)


count_languages = Counter(languages)
for key, value in count_languages.items(): 
    print(key + " is the language of " + str(value) + " books ")
