#!/usr/bin/env python3

s = input("Enter a sentence: ")
first_char = s[0]
first_char_count = s.count(first_char)
last_char = s[-1]
last_char_count = s.count(last_char)

print("first char:", first_char)
print("first char count:", first_char_count)

print("last char:", last_char)
print("last char count:", last_char_count)

