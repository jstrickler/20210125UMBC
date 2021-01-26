#!/usr/bin/env python3

words = [
    'abc',
    '123',
    'abc123',
    '56909430',
    'wombats!',
    '897',
]

def is_numeric(s):
    return s.isdigit()

numeric_words = filter(is_numeric, words)
print(words)
for word in numeric_words:
    print(word)

