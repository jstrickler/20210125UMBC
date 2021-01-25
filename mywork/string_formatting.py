#!/usr/bin/env python3

name = "Fred"
rating = 23.3397

print(name, rating)
print("Name: {} Rating: {}".format(name, rating))
print("Name: {} Rating: {:.2f}".format(name, rating))
print(f"Name: {name} Rating: {rating:.2f}")

count = 35

print("Count: {:05d}".format(count))
print(f"Count: {count:05d}")


print("Count: {:5d}".format(count))

n = 2309582305823058203582093589.32
print("Big number: {:,f}".format(n))

