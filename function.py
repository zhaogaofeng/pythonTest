from myabstest import *


def fact(n):
    if not isinstance(n, (int)):
        raise TypeError('fd')
    if n == 1:
        return 1
    return fact(n - 1) * (n)

print(fact)


def myPower(m, n=2):
    s = 1
    while n > 0:
        n=n-1
        s = s * m

    return s
print(myPower(2))
