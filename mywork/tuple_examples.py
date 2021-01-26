
person = "Bill", 'Gates', 'Microsoft', '1955-10-24'

print(person)
print(person[0], person[1])

a = 1, 2, 3
b = [1, 2, 3]
print(type(a), type(b))

x = [(1, 2), (3, 4), (8, 11)]

print(x[0])

for i, field in  enumerate(person):
    print(i, field)

print(list(enumerate(person)))

for m, n in x:
    print(m, n * 10)


x = 45

y = 7

result = divmod(x, y)
print(result)
result, remainder = divmod(x, y)

print(result, remainder)
print("this is a test")

people = [
    ('Joe', 'Schmo', 'Laurel', 'MD'),
    ('Karen', 'Killarney', 'Pasadena', 'MD'),
    ("Bob", "Boies", 'Manassa', 'VA'),
    ("Clem", "Kadiddlehopper", "Strasburg", "VA"),
]

print(people)
print(people[0])
print(people[0][0])

for person in people:
    print(person[0], person[1])
print("-" * 60)

for person in people:
    first_name, last_name, city, state = person
    print(first_name, last_name)
print("-" * 60)

for first_name, last_name, city, state in people:
    print(first_name, last_name)
print("-" * 60)

colors = ['red', 'green', 'mauve', 'ochre']
print(list(enumerate(colors)))
for index, color in enumerate(colors):
    print(index, color)
