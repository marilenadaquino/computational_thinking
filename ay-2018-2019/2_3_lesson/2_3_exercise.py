import csv

listTitles , sexPistols , after2000 , languages = [] , [] , [] , []

with open('titles.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)    
    for row in reader: 
        listTitles.append(row['Title'])

sortedListTitles = sorted(listTitles)
print(sortedListTitles)