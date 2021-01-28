#!/usr/bin/env python3
""" A Solution For functions_ex01
    Write a program that counts the number of lines, words, and characters in
    each file named on the command line.
"""

from sys import argv
fmt = "{:20} {:^5} {:^5} {:^5}"
print(fmt.format("FILE NAME", "LINES", "WORDS", "CHARS"))

del argv[0]
total_only = False
if '-t' in argv:
    total_only = True
    argv.remove('-t')

total_lines = total_chars = total_words = 0
for filename in argv:
    with open(filename, "r") as f:
        lines = words = chars = 0
        for line in f:
            lines += 1
            chars += len(line)
            data = line.split()
            words += len(data)
        if total_only:
            total_lines += lines
            total_chars += chars
            total_words += words
    if not total_only:
        print(fmt.format(filename, lines, words, chars))

if total_only:
    print(fmt.format('TOTAL', total_lines, total_words, total_chars))


