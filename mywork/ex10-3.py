#!/usr/bin/env python3
import math

nums = range(1, 11)

x = {n:  math.factorial(n) for n in nums}

result = x[6] * x[5]

print("result: {}\n".format(result))

