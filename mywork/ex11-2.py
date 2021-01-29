#!/usr/bin/env python3
import re

pattern = r"^([+-]?)\d+\.\d+$"

while True:
    number = input("Enter a float (or q to quit): ")
    if number == 'q':
        break

    m = re.search(pattern, number)
    if m:
        if m.lastindex == 1 and m.group(1) == '-':
            sign = "negative"
        else:
            sign = "positive"
        print("Valid float is", sign)
    else:
        print("That is not a float!")
