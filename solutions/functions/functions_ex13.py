#!/usr/bin/env python3
""" A Solution For functions_ex13
    While the index method of a list can be used to find either the first
    occurrence of an item or the first occurrence of it within a range of
    the list, it does not allow you to find, say the second or third
    occurrence by passing in a number as to the one you are looking for.
    • Write a function that takes 2 parameters; one being the list to search,
      and the other being an  int representing which one you are looking for
      such as the fist, second, third occurrence.
    • The index method raises a ValueError exception if the value being
      searched for does not exit in the list.
    • It is perfectly fine for your function to behave in the same manner.
"""


items = ['a', 'b', 'a', 'a', 'c', 'd', 'e', 'f', 'a']

def index_nth(items, target, nth):
   count = 0
   for i, item in enumerate(items):
      if target == item:
           count += 1
           if count == nth:
              return i
          
   return -1

pos = index_nth(items, 'f', 1)
print(pos)

target = 'a'
nth = 3
print(list(enumerate(items)))
print(list(filter(lambda x: x[1] == target, enumerate(items)))[nth][0])