
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

def fib():
	x,y = 0,1
	while True:
		yield x
		x, y = y, x+y

def even(sequence):
	for number in sequence:
		if number % 2 == 0:
			yield number

def under_4_mil(sequence):
	for number in sequence:
		if number > 4000000:
			break
		yield number

print sum(even(under_4_mil(fib())));