#!/usr/bin/env python3

s = input("Enter a string: ")
print("Ends with period?", s.endswith('.'))
print("Only alphas?", s.isalpha())
print("x in string?", 'x' in s.lower())
s2 = s.replace('e', 'E')
print(s2)
