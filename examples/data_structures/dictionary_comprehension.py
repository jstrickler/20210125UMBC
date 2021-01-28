#!/usr/bin/env python3

foods = ['spam', 'spam', 'toast', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 
'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'toast', 'haggis',
'spam', 'spam', 'haggis', 'bacon', 'toast', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]


def main():
    names = ["Ashley", "Emma", "Jayden", "Ethan"]
    d = {name: len(name) for name in names}
    print(d)

    good_foods = {f for f in foods if f not in ('spam', 'haggis')}
    print("good_foods: {}\n".format(good_foods))
    
    



if __name__ == "__main__":
    main()   # Output: {'Jayden': 6, 'Ethan': 5, 'Ashley': 6, 'Emma': 4}

