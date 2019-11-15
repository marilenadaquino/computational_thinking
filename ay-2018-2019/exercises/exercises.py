
# exercise 1
def exercise1():
	l=[]
	for i in range(2000, 3201):
	    if (i%7==0) and (i%5!=0):
	        l.append(str(i))

	print ','.join(l)

exercise1()

# exercise 2
expectedOutput = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# exercise 3
def exercise3(a):
	n1 = int( "%s" % a )
	n2 = int( "%s%s" % (a,a) )
	n3 = int( "%s%s%s" % (a,a,a) )
	n4 = int( "%s%s%s%s" % (a,a,a,a) )
	print n1+n2+n3+n4

exercise3(9)


# exercise 4
def exercise4(s):
	operations = s.split(",")
	netAmount = 0
	for operation in operations:
		values = operation.split(" ")
		operation = values[0]
		amount = int(values[1])
		if operation=="D":
			netAmount+=amount
		elif operation=="W":
			netAmount-=amount
		else:
			pass
	print str(netAmount)

exercise4('D 300,D 300,W 200,D 100')


# exercise 5
def f(n):
	if n == 0: 
		return 0
	elif n == 1: 
		return 1
	else: 
		return f(n-1)+f(n-2)

print f(int(7))


# exercise 6
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(7)
values = [str(f(x)) for x in range(0, n+1)]
print ",".join(values)