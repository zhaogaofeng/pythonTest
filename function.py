from myabstest import *
def fact(n):
	if not isinstance(n,(int)):
		raise TypeError('fd')
	if n==1:
		return 1
	return fact(n-1)*(n)


print(fact(10))