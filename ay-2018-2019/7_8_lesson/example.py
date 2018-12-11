from collections import defaultdict
import pprint


myTup = ('Silvio', 'is')
myTup2 = ('very','old')
myNewTup = myTup + myTup2
print('\n1 print a tuple:\n',myNewTup)
print('\n2 print all items of a tuple:')
for w in myNewTup:
	print(w)

city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

# iterate over items of a list of tuples
print('\n3 print all the second items of tuples included in a list')
for couple in city_list: # declare one variable to define the tuple
	print('city: ',couple[1]) # use the slicing notation to get items in the tuple

print('\n4 print all the first items of tuples included in a list')
for first, second in city_list: # declare a variable for each item in the tuple
	print('country: ', first)

print('\n5 create a defaultdict including items of the list of tuples grouped by the the first item of the tuples')
# create a default dict from the above list of tuples
cities_by_state = defaultdict(list)
for state, city in city_list:
	cities_by_state[state].append(city)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(cities_by_state)