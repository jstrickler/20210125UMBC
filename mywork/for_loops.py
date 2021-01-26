#!/usr/bin/env python3

#  for VAR in ITERABLE:
#      ...use VAR...

s = "abc"
for ch in s:
    print(ch)
print()

#  range(STOP)  range(START, STOP)  range(START, STOP, STEP)

for i in range(5):
    print(i)
print()

print(range(1000000))

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')

for i in range(-20, 21, 5):
    print(i, end=",")
print('\n')

for i in range(20, -21, -5):
    print(i, end=",")
print('\n')

for i in range(65,91):
    print(i, chr(i))
print()

data = "5 18 37 3 9"

raw_values = data.split()
print(raw_values)

for raw_value in raw_values:
    value = int(raw_value)
    print(value * 10)


raw_line = "5:8:42.9:16:44\n"

raw_nums = raw_line.rstrip().split(':')
print(raw_nums)

for raw_num in raw_nums:
    num = float(raw_num)
    print(raw_num, raw_num * 5, num * 5)

#  r = range(....)
#  r is a GENERATOR
r = range(10)
print(r)
for i in r:
    # i = next value of r
    print(i, end=' ')
print('\n')

# for VAR in ITERABLE-THINGY:
#     do something with VAR

values = ["alpha", "beta", "gamma"]
for v in values:
    # v = values[0]
    # v = values[1]
    # v = values[2]
    print(v)
print()


for wombat in range(8):
    print(wombat)
print('\n')

#  iterables: range() list generator tuple  AND OTHERS

for name in 'Billy', 'Bob', 'Charlie':
    print("Hello,", name)
print()

for num in range(8):
    print("Don't give up -- Python is fun!")

# range(5)  range(1, 11)  range(2, 21, 2)

colors = ['red', 'blue', 'green']
for c in colors:
    print(c)
print()

colors = 'red blue green'.split()

print(colors)

for color in colors:
    print(color)



























