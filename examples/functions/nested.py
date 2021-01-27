#!/usr/bin/env python3
def outer(a, b):
    x = 15
    y = 20

    def inner(z):
        print(g, a, b, x, y, z)  #  a, b, x and y are nonlocal   z is local  g is global

    print("ID of inner:", id(inner))

    return inner  # a reference to inner function

g = "my global data"
result = outer(5, 10)
print(type(result), id(result))
result(9)  # invoke the returned function
