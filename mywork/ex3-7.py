#!/usr/bin/env python3

for i in range(0, 41, 10):
    for j in range(i, i + 10):
        print(f"{j:2d}", end=' ')
    print()

print(list(range(1, 10)))
print(list(range(5)))
print(list(range(2, 11, 2)))

total = 0
for n in range(10):
    total = total + n
    # total += n
print(total)

print(sum(range(10)))
