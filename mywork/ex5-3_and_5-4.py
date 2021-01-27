#!/usr/bin/env python3

# ex5-3
def get_sum(*args):
    total = 0
    for num in args:
        total += num
    
    return total

result = get_sum(2, 9, 3, 8, 14)
print(result)

# ex5-4
def get_sum_avg(*args):
    total = 0
    for num in args:
        total += num
    if len(args) == 0:
        return 0
    avg = total / len(args)

    return total, avg

s, a = get_sum_avg(2, 9, 3, 8, 14)
print(s)
print(a)

x = get_sum_avg(5, -4, 18, 99, 44, 2177, -3, 8.27)
print(x)


