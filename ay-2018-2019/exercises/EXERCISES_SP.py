# checking numbers
def is_odd(int_number):
	""" Write the function def is_odd(int_number) in Python that takes an integer number as
	input and returns True if the number is odd, False otherwise."""
	if int_number%2 == 0:
		return True
	else:
		return False

print 'checking numbers:', is_odd(2) 

# Floor division
def floor_division(dividend, divisor):
	"""Write the function def floor_division(dividend, divisor) that takes the dividend
	and the divisor as input and returns the division between the two and returns only the integer
	part of the division, without considering the fractional part. For instance, 5/2 will return 2, as well
	as 6/3. Note that it is not possible to use the Python built-in operator // in the algorithm
	implementation."""
	return int(dividend/divisor)

print 'Floor division:', floor_division(5,2) 

# Finding the maximum
def find_max(number_collection):
	"""Write the function def find_max(number_collection) that takes a collection (a list, a
	set, etc.) of numbers as input and returns the greatest number it contains."""
	max_value = 0
	for num in number_collection:
		if num > max_value:
			max_value = num
	return max_value

print 'Finding the maximum:', find_max([1,2,3,4,5,6,7,8])

#Finding the minimum
def find_min(number_collection):
	"""Write the function def find_min(number_collection) that takes a collection (a list, a
	set, etc.) of numbers as input and returns the lowest number it contains."""

	min_value = number_collection[0]
	for num in number_collection:
		if num < min_value:
			min_value = num
	return min_value

print 'Finding the maximum:', find_min([1,2,3,4,5,6,7,8])

# Prime factorization (brute force)
def prime_factorization(n):
	"""Write the function def prime_factorization(int_number) that takes an integer number
	as input and returns its prime factorization, i.e. a dictionary specifying as keys the prime factor
	numbers of the input integer and as keys how many times that prime number is actually used in
	the factorization. For instance, the prime factorization of the number 60 is 5 * 3 * 2 * 2, thus
	resulting in the following dictionary: {5: 1, 3: 1, 2: 2}."""
	i = 2
	factors = []
	while i * i <= n:
		if n % i: 
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n) 
	from collections import Counter
	return Counter(factors)

print 'Prime factorization:', prime_factorization(60) 

# Palindromos
def is_palindromic(word):
	"""Write the function def is_palindromic(word) that takes a word as input and returns True
	if it is a palindrome, False otherwise. For instance, "anna" and "madam" are both palindromic
	words."""
	if word[::-1] == word:
		return True
	else:
		return False
print "Palindromos:", is_palindromic('anna')

# Common substring (dynamic programming)
# discussion: https://stackoverflow.com/questions/18715688/find-common-substring-between-two-strings
def longest_common_substring(string1, string2):
	"""Write the function def longest_common_substring(s1, s2) that takes two strings as
	input and returns a new string which is the longest common substring contained in both the
	input strings. For instance, specifying the strings "this is new, guys!" and "it is
	new, fellows!" as input, the algorithm should return the string " is new, ". If no
	common substring exists, the empty string "" is returned."""
	answer = ""
	len1, len2 = len(string1), len(string2)
	for i in range(len1):
		match = ""
		for j in range(len2): # finda a match
			if (i + j < len1 and string1[i + j] == string2[j]):
				match += string2[j]
			else: # replace match with the longest one found
				if (len(match) > len(answer)): 
					answer = match
				match = ""
	return answer

print "Common substring: '"+ longest_common_substring("this is new, guys!", "it is new, fellows!")+ "'"

# String distance
# explanation: https://www.python-course.eu/levenshtein_distance.php
def levenshtein_distance(s1, s2):
	"""Write the function def levenshtein_distance(s1, s2) that takes two strings as input
	and returns the minimum number of edit operations on characters that are needed to transform
	the first string into the second one. For instance, considering the strings "house" and "home",
	the function should return 2: substitute the character u with the character m (first operation:
	"house" -> "homse"), and remove the character s (second operation: "homse" ->
	"home")."""
	if s1 == "":
		return len(s2)
	if s2 == "":
		return len(s1)
	if s1[-1] == s2[-1]:
		cost = 0
	else:
		cost = 1
	res = min([levenshtein_distance(s1[:-1], s2)+1, levenshtein_distance(s1, s2[:-1])+1, levenshtein_distance(s1[:-1], s2[:-1]) + cost])
	return res
print "String distance:", levenshtein_distance("house", "home")


# Another distance metric for strings
def hamming_distance(s1, s2):
	"""The Hamming distance between two strings of equal length is the number of positions at which
	the corresponding characters are different. Thus, it measures the minimum number of
	substitutions required to change one string into the other.
	Write the function def hamming_distance(s1, s2) which takes two strings as input and
	that calculates the Hamming distance if the strings have the same length, otherwise it returns
	the smallest string."""
	diffs = 0
	if len(s1) == len(s2):
		for ch1, ch2 in zip(s1, s2):
			if ch1 != ch2:
				diffs += 1
		return diffs
	elif len(s1) < len(s2):
		return s1
	else:
		return s2

print "Another distance metric for strings:", hamming_distance('house','cause')