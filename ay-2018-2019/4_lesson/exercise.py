import json

female_artists = {}
female_artists_IIWW = []

with open('ArtistsMoMA.json','r', encoding='utf8') as my_list_of_dictionaries:
	data = json.load(my_list_of_dictionaries)
	for artist in data:
		# Print all the artists' names
		print(artist['DisplayName'])
		# # Print the names of Italians artists
		if artist['Nationality'] == 'Italian':
			print(artist['DisplayName'])
		# # Print the names of Italians artists born after 1923
		if artist['Nationality'] == 'Italian' and artist['BeginDate'] > 1923:
			print(artist['DisplayName'])
		# # Print the names of Italians female artists born after 1923
		if artist['Gender'] == 'Female' and artist['BeginDate'] > 1923:
			print(artist['DisplayName'])
		# Create a new dictionary including names and birth dates of female artists born after 1900.
		if artist['Gender'] == 'Female' and artist['BeginDate'] > 1900:
			female_artists[artist['DisplayName']] = artist['BeginDate']

		# Create a new dictionary including all the female artists that during the WWII were in their twenties.
		if artist['Gender'] == 'Female' and (artist['BeginDate'] >= 1915 and artist['BeginDate'] <= 1925):
			female_artists_IIWW.append(artist)

# for artist in female_artists_IIWW:
# 	print(artist['ConstituentID'])

# Print all the birth dates included in the new dictionary.
for artist, date in female_artists.items():
	print(artist.encode('utf8'))