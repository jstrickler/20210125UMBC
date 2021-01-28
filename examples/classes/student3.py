#!/usr/bin/env python3

class InvalidMajorError(Exception): pass

class Student:   # inherits from object  by default

    def __init__(self, name, major):
        self.name = name    # Calls the @name.setter method
        self.major = major  # Calls the @major.setter method

    @property  # decorator
    def name(self):  # getter property
        return self._name

    @name.setter  # decorator
    def name(self, name):  # setter property
        if isinstance(name, str):
        # print("Debug:", "name setter being called")
            self._name = name
        else:
            raise TypeError("name must be a string")

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        # print("Debug:", "major setter being called")
        self._major = major

if __name__ == "__main__":
    s = Student("Bob", "Animal Husbandry")
    print(s.name)   # call s.name()
    s.name = "Fred"  # call s.name("Fred")
    print(s.name)
    print(s)  # print(str(s))    Student.__str__(s)  object.__str__(s)



