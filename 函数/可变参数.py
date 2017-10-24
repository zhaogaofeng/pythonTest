def calc(*num):
    sum = 0
    for i in num:
        sum = sum + i * i
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person("nike",30,**extra))