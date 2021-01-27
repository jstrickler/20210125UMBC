#!/usr/bin/env python3

# new_list = filter(FUNC, ITERABLE)
results = filter(lambda x: x % 3 == 0, range(2, 51))

for value in results:
    print(value, end=' ')
print()


fruits = ['fig', 'pomegranate', 'apple', 'lemon',
'pear', 'papaya', 'lime', 'kiwi', 'cherry', 'banana']

f1 = sorted(fruits)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=len)
print("f2:", f2, '\n')

def mysort(f):
    return len(f), f

f3 = sorted(fruits, key=mysort)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=lambda f: (len(f), f))
print("f4:", f4, '\n')

people = [
    ('Joe', 'Schmo', 'Laurel', 'MD'),
    ('Karen', 'Killarney', 'Pasadena', 'MD'),
    ("Bob", "Boies", 'Manassas', 'VA'),
    ("Clem", "Kadiddlehopper", "Strasburg", "VA"),
]

for person in sorted(people, key=lambda p: p[2]):
    print(person)
print()









