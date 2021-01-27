#!/usr/bin/env python3
"""
Miscellaneous functions


These are some awesome demo functions and data for UMBC Python class 
"""
def main():
    print("Testing my functions at top level", square(5), cube(10))

COLORS = ['red', 'blue', 'green']

def square(p):
    """
    Return the square of a number

    Will raise TypeError on non numeric arguments.

    :param p: number to square
    :return: squared result
    """
    return p ** 2



def cube(p):
    """
    Return cube of specified number.
    """
    return p ** 3

print("in reusable.py: my name is", __name__)

if __name__ == "__main__":  # if this script is run directly, NOT imported
    print("HI MOM!!!")
    main()

