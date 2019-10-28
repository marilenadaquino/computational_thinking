# -*- coding: utf-8 -*-
import csv , sys

# prepare lists including results
listTitles = [] 
sexPistols = []
after2000 = [] 
languages = []


with open('titles.csv', 'r', encoding="utf8") as myfile: # open a csv file
    sys.stdout
    reader = csv.reader(myfile) # each row of the file is a list
    for row in reader: # access each row / list of the file at the same time
        listTitles.append(row[0])
        if ("sex pistols" in row[0].lower() ) or ("sex pistols" in row[1].lower()) or ("sex pistols" in row[23].lower()):
        	sexPistols.append(row[0])
        if int(row[18]) >=2000:
        	after2000.append(row[0])
        languages.append(row[25])

# 1. Print all titles
print(listTitles)

# 2. Print all titles sorted in alphabetical order 
sortedListTitles = sorted(listTitles)
print(sortedListTitles)

# 3. Print all the titles of references talking _somehow_ about Sex Pistols, i.e. including the words "Sex Pistols"
print(sexPistols)

# 4. Print all the titles of references published after 2000
print(after2000)

