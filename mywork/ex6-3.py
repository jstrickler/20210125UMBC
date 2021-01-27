#!/usr/bin/env python3
import sys

print(sys.argv)  # list of parameters (words) on command line 
#  sys.argv[0]  script name
# sys.argv[1] 1st "real" param

for arg in sys.argv[1:]:  # list without first element
    print(arg)
print()

args = sys.argv[1:]  # skip the command name

script_name = sys.argv.pop(0)  # remove first element (i.e. script name)
print(script_name)
print(sys.argv)  # args without script name

sorted_args = sorted(sys.argv)


for arg in sorted_args:
    print(arg, end=" ")
print()

print(",".join(sorted_args))


