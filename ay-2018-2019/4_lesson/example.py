# create a dictionary
my_dict = {}
my_dict = {'fruit1': 'apple', 'fruit2': 'orange'}
print('example 1 \n', my_dict) # NB. do not use + when concatenating different types of data (i.e. string and dictionary)

# add a key:value pair to the dictionary
my_dict['fruit3'] = 'bananas'
print('example 2 \n', my_dict)

# update the value of a pair
my_dict['fruit3'] = 'banana'
print('example 3 \n',my_dict)

# add more pairs at once
another_dict = {}
yet_another_list = ['apple','orange','strawberry','pineapple','blueberry']
n = 0
for fruit in yet_another_list:
	n += 1
	another_dict['fruit'+str(n)] = fruit
print('example 4 \n', another_dict)

# access the value of a pair by calling the unique key
print('example 5 \n', my_dict['fruit1'])

# access all key/value pairs
print('example 6')
for k,v in another_dict.items():
	print(k, ' has value ', v)

# access only keys
print('example 7')
for k in another_dict.keys():
	print(k)

# access only values
print('example 8')
for k in another_dict.values():
	print(k)

# access a value when this is a list item
dictionary_with_list = {'fruit': 'apple', 'smallfruits': ['strawberry','blueberry']}
print('example 9\n', dictionary_with_list['smallfruits'][0])

# access all the values in a list of dictionaries
print('example 10')
list_of_dictionaries = [{'fruit': 'apple'},{'fruit': 'orange'},{'fruit': 'banana'}, {'fruit': 'pineapple'}]
for fruitDict in list_of_dictionaries:
	print(fruitDict['fruit'])

# access all key/value pairs of a sorted dictionary
print('example 11')
for k,v in sorted(another_dict.items()):
	print(k, ' has value ', v)