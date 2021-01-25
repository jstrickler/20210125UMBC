#!/usr/bin/env python3
import sys

x = 5
X = 10

print(x, X)

x = 10
y = 20

print(
    "supercalifragilisticexpialidocious",
    "wombats",
    "pine martens",
    "more junk"
)

input_file = "warthogs.txt"

x = 22
y = 18.23902
z = "zebra"

print(x, y, z)
print(str(x) + ' ' + str(y) + ' ' + str(z) + '\n')

print(x, y, z, sep=":")
print(x, y, z, sep="")
print(x, y, z, sep=" <=> ")

print(x, end=' ')
print(y, end=' ')
print(z)

print("Help help!!", file=sys.stderr)










