# Write a Python program to calculate the sum of a list of numbers.
# let's do iteratively first
def list_sum1(num_List):
	total = 0
	for el in num_List:
		total += el
	return total
print('list_sum1:', list_sum1([2, 4, 5, 6, 7]))


def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
        
print('list_sum:',list_sum([2, 4, 5, 6, 7]))


# Write a Python program of recursion list sum.
def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))


# Write a Python program to find the greatest common divisor (gcd) of two integers
def Recurgcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return Recurgcd(low, high%low) # remainder of the division
print(Recurgcd(12,14))