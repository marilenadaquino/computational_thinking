# Exercises

## exercise 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

## exercise 2

What is the result of the following function if the input is n=8?

def exercise2(n):
	d=dict()
	for i in range(1,n+1):
		d[i]=i*i
	print d

## exercise 3

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9
The output should be: 11106


## exercise 4

Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300,D 300,W 200,D 100. The output should be: 500.

## exercise 5

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Write a program to compute the value of f(n) with a given n.

E.g. If 7 is given as input to the program, the output should be: 13


## exercise 6
Write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

If the 7 is given as input to the program, the output of the program should be: 0,1,1,2,3,5,8,13