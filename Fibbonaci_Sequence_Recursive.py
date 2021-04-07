def fib(n): # Fibbonaci sequence
if n <= 1:
	return n
else:
	return (fib(n-1) + fib(n=2))
	
terms = int(input())

if terms <= 0: # See if there are enough terms
	print('you stupid')
else:
	for i in range(terms):
		print(fib(i))
