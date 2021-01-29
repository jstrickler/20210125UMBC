#!/usr/bin/env python3

def hello():
    print("Hello, world")

def spam():
    print("Hello from spam")


def clean_up(s):
    return s.lower().strip()


hello()
spam()

s1 = "    Wildebeest    "
s2 = clean_up(s1)
print("|" + s2 + "|")
