#!/usr/bin/env python3
import sys

args = sys.argv[1:]

total = 0
for raw_num in args:
    num = float(raw_num)
    total += num

print("sum:", total)
average = total / len(args)
print("average:", average)