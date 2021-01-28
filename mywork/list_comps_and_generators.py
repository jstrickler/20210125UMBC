#!/usr/bin/env python3

fruits = ['apple', 'banana', 'kiwi', 'peach', 'lime', 'lemon', 'papaya', 'persimmon',
'mango', 'date', 'elderberry', 'watermelon', 'pomegranate']

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

f00 = []
for f in fruits:
    if f.startswith('p'):
        f00.append(f.upper())
print("f00: {}\n".format(f00))

f000 = []
for f in fruits:
    if f.startswith('p'):
        f000.append(f)
print("f000: {}\n".format(f000))

#  [EXPR for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]  
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

foods = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 
'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'toast', 
'spam', 'spam', 'haggis', 'bacon', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

x = 'wombat'
good_foods = [f for f in foods if f != 'spam']
print("good_foods: {}\n".format(good_foods))

abbrs = [f[:3] for f in fruits]
print("abbrs: {}\n".format(abbrs))

lengths = [len(f) for f in fruits]
print("lengths: {}\n".format(lengths))

nums = [5, 8, -2, 4.383, 0, 15]

squares = [n ** 2 for n in nums if isinstance(n, int)]
print("squares: {}\n".format(squares))

squares = [n ** 2 for n in nums if isinstance(n, int) if n > 0]
print("squares: {}\n".format(squares))

things = [(n, n**2, n**3) for n in range(10)]
print("things: {}\n".format(things))

values = ['123', '89', '48', '17', '8', '0', 'abc', '873']

ints = [int(v) for v in values if v.isdigit()]
print("values: {}\n".format(values))
print("ints: {}\n".format(ints))

fgen = (f.upper() for f in fruits)
print(fgen)
for fruit in fgen:
    print(fruit, end=' ')
print()

good_foods_gen = (f.upper() for f in foods if f != 'spam')

for good_food in good_foods_gen:
    print(good_food)