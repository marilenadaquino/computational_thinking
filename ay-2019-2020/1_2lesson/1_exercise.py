# -*- coding: utf-8 -*-
import csv

# prepare lists including results
listTitles = []
sexPistols = []
after2000 = []
languagesafter2000 = []
uniqueAuthors = []

with open('titles.csv', 'r', encoding="utf8") as myfile: # open a csv file
    reader = csv.reader(myfile) # each row of the file is a list
    for row in reader: # access each row / list of the file at the same time
        listTitles.append(row[0])
        if ("sex pistols" in row[0].lower() ) or ("sex pistols" in row[1].lower()) or ("sex pistols" in row[23].lower()):
        	sexPistols.append(row[0])
        if int(row[18]) >=2000:
        	after2000.append(row[0])
        if row[25] == 'English' and int(row[18]) >=2000:
            languagesafter2000.append(row[0])
        author = row[8]
        if author not in uniqueAuthors:
            uniqueAuthors.append(author)


# 1. Print all titles
print(listTitles)

# 2. Print all titles sorted in alphabetical order
sortedListTitles = sorted(listTitles)
print(sortedListTitles)

# 3. Print all the titles of references talking _somehow_ about Sex Pistols, i.e. including the words "Sex Pistols"
print(sexPistols)

# 4. Print all the titles of references published after 2000
print(after2000)

# 5. Print all the titles of references published after 2000 that are written in english
for title in languagesafter2000:
    print(title)

# 6. Print all the authors' names (without repetitions)
for author in uniqueAuthors:
    print(author)
