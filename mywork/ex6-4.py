#!/usr/bin/env python3
import sys

total = 0
for raw_num in sys.argv[1:]:
    num = float(raw_num)
    total += num

print("sum:", total)
average = total / (len(sys.argv) -1 )
print("average:", average)