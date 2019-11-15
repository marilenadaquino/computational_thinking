import csv , pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=2)

dictDewey = defaultdict(set)
with open('topics.csv','r') as fileCsv:
	reader = csv.DictReader(fileCsv)
	for row in reader:
		dictDewey[row['Dewey classification']].add( (row['Type of topic'], row['Topic']) )

#pp.pprint(dictDewey)

# create a clean dictionary
dictId= defaultdict(set)
with open('topics.csv', 'r') as fileCsv:
	reader = csv.DictReader(fileCsv)
	for row in reader:
		dictId[row["Content type"].encode('utf8')].add(row["BL record ID"])

print(dictId)