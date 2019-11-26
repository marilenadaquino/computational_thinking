import csv , pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=2)

# create a dictionary where the key is the DDC identifier and the value is a list of tuples

def doMystuff(textName):
	""" a function that returns nice lists"""

	dictDewey = defaultdict(set)
	with open(textName, 'r', errors='ignore') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:

	    	dictDewey[row['Dewey classification']].add((row['Type of topic'],row['Topic']))
	pp.pprint(dictDewey)

	# create a clean dictionary
	cleanDict = defaultdict(dict)
	for ddc, stuff in dictDewey.items():
		for typeTopic, topic in stuff:
			if typeTopic not in cleanDict[ddc] and topic not in cleanDict[ddc]:
				cleanDict[ddc][typeTopic] = [topic]
			if topic not in cleanDict[ddc][typeTopic]:
				cleanDict[ddc][typeTopic].append(topic)

	pp.pprint(cleanDict)

	# print the bullet list
	for ddc, types in cleanDict.items():
		print('-',ddc+':')
		for typeTopic, listTopics in types.items():
			print('   -',typeTopic+':')
			for topic in listTopics:
				print('      -',topic)

	# reproduce the physical organization at the British Library
	dictCollocation = defaultdict(set)
	with open(textName, 'r', errors='ignore') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	    	dictCollocation[row['Content type']].add(row['BL record ID'])

	pp.pprint(dictCollocation)

	# print the bullet list
	for key,values in dictCollocation.items():
		print('- '+key+':')
		for value in values:
			print('		- '+value)

doMystuff('topics.csv')
