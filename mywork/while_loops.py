#!/usr/bin/env python3

i = 0
while i < 5:
    print("i is", i)
    i += 1
print()

while True:
    user_name = input("What is your name (or q to quit)? ")
    if user_name == 'q':
        break
    if user_name == '':
        print("Please enter one or more characters")
        continue
    print("Welcome,", user_name)

