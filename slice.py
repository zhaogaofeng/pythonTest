
import os
L=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
a=[m + n for m in 'ABC' for n in 'XYZ']
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
	print(k,'=',v)
L1 = ['Hello', 'World', 18, 'Apple', None]
a=[s.lower() for s in L1 if isinstance(s,str)]
print(a)