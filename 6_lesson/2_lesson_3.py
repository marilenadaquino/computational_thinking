# coding: utf-8
import csv , re
from collections import Counter

def findDuplicates(inputFile, fieldName):
	''' given a csv file in input and a field name for disambiguating records,
	returns a list of duplicates'''
	listDisambiguate = []

	with open(inputFile, 'r', errors='ignore') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader: # iterates over the lines in the .csv file / i.e., key, value of the dictionary
			listDisambiguate.append(row[fieldName]) # look into a column and create a list
		
		duplicates = [item for item, count in Counter(listDisambiguate).items() if count > 1]
		# duplicates = [item for n, item in enumerate(listDisambiguate) if item in listDisambiguate[:n]] # find the duplicates and add them to a new list
		# duplicates = [_f for _f in duplicates if _f] # remove blank elements from duplicates ; [x for x in duplicatesISBN if x] alternative way
		# duplicates = list(set(duplicates)) # remove duplicate from the list of duplicates

		print('\nDuplicates in list:')
		for dupl in duplicates:
			print((fieldName+':'+dupl))

def cleanListOfDict(oldList):
	''' given a list of dictionaries with duplicate items
	returns a new cleaned list of dictionaries'''
	newList = [] # create a new empty list to store the cleaned dictionaries
	for i in range(0, len(oldList)): # iterate over the length of the list of dictionaries
		if oldList[i] not in oldList[i+1:]: # look for duplicates in following dictionaries
			newList.append(oldList[i]) # add the unique ones to the new list
	print(newList)

def cleanAuthors(inputFile, fieldName):
	''' given a list of authors in the form lastName, firstName 
	returns the same list cleaned and ready to be integrated in a bibliographic citation in Chicago style'''
	
	authors , cleanAuthors = [] , [] # create a list with authors, prepare the list to store the cleaned list of authors
	
	with open(inputFile, 'r', errors='ignore') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader: 
			authors.append(row[fieldName])

	for auth in authors: 
		if ';' in auth: # multiple authors
			splitList = auth.split(';') # split a group of authors by semicolon
			splitList = [au for au in splitList if 'organisation' not in au]
			for au in splitList: #iterate over each single author					
				splitList2 = au.split(',') # split parts of the name of a single author by comma
				if len(splitList2) >=3: # after removing organisations, if there are still more than one author
					del splitList2[2:] # delete the substring after the third comma if exists (e.g. author, writer)
					splitList = [auth.replace(au, ', '.join(aux.strip() for aux in splitList2))] 
				if (len(splitList2) == 2) and ('artist' in splitList2[1] or 'author' in splitList2[1]) : # delete artist when in second position
					del splitList2[1]
					splitList = splitList2
				auth = ';'.join(au for au in splitList if au != ' ')
			
			splitList = auth.split(';') # update the list

			if len(splitList) >= 2:
				for i in splitList[0]:
					i = i.strip()
				for i in splitList[1:]:
					if ',' in i:
						splitList2 = i.split(',')
						splitList2[0], splitList2[1] = splitList2[1], splitList2[0] # swap last name and first name
						splitList = [auth.replace(i, ' '.join(i for i in splitList2))] # update list of split names
						auth = ', '.join(au for au in splitList if au != ' ') # update list of authors

				splitList = auth.split(';') # split again the (updated) list of multiple authors
				splitList[-1] = str(' and'+splitList[-1]) # add "and" before the last author, after swapping last/first name
				auth = ';'.join(au for au in splitList if au != ' ') # update the list
		# single author
		else:
			splitList = auth.split(',') # split parts of the name of a single author by comma
			if len(splitList) >=3:
				del splitList[2:]
				splitList = [auth.replace(auth, ', '.join(aux.strip() for aux in splitList))]
			if (len(splitList) == 2) and ('artist' in splitList[1] or 'author' in splitList[1]) : # delete artist when in second position
				del splitList[1]
			auth = ','.join(au for au in splitList) 
		if len(auth) == 0: # substitutes empty authors with -
			auth = '-' 
		auth = re.sub("\s?[\(\[].*?[\)\]]\s?", "", auth) # remove [], () and text included 
		auth = re.sub("\,?\s?\d+\-?", "", auth) # remove digits and if exist, following - and ,
		auth = re.sub(';',',',auth) # finally remove the ;
		auth = auth+'.'
		cleanAuthors.append(auth)

	return cleanAuthors

def chicagoCitation(inputFile, authors, title, city, publisher, date):
	''' given a csv file and fieldnames including all the elements of a bibliographic reference 
	returns the bibliographic citation in Chicago style'''

	with open(inputFile, 'r', errors='ignore') as csvfile:

		authorsList = cleanAuthors(inputFile, authors)
		titlesList , citiesList , publishersList , datesList = [] , [] , [] , [] # create lists

		reader = csv.DictReader(csvfile)
		for row in reader: 

			titlesList.append(row[title])
			citiesList.append(row[city])
			publishersList.append(row[publisher])
			datesList.append(row[date])
		
		citations = list(zip(authorsList, titlesList, citiesList, publishersList, datesList))
		for citation in citations:
			if citation[3] is '':
				print(citation[0]+' '+citation[1]+'. '+citation[4]+'.')
			else:
				print(citation[0]+' '+citation[1]+'. '+citation[2]+': '+citation[3]+', '+citation[4]+'.')
			

# declare variables and call the functions
csvfile = 'titles.csv'
#findDuplicates(csvfile, 'ISBN')

# anotherList = [{'a': 123}, {'b': 123}, {'a': 123}]
# cleanListOfDict(anotherList)

# cleanAuthors(csvfile, 'All names')
chicagoCitation(csvfile, 'All names', 'Title', 'Place of publication', 'Publisher', 'Date of publication')