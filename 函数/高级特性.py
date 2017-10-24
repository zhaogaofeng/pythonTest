from collections import Iterable
L = ('Michael', 'Sarah', 'Tracy', 'Bob', 'Jack')
print(L[-2:])
L = list(range(100))
print(L[:2:5])
print(isinstance("fd", Iterable))
for i, value in enumerate(L):
    print(i, value)
for x, y in [(2, 3), (4, 5)]:
    print(x, y)
print(range(10))
L = list(range(1, 11))
L = (x * x for x in range(1, 11))
print(L)
for l in L:
	print(l)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)

def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return "done"
print(fib(5))