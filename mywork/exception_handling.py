colors = ['red', 'purple', 'green', 'orange']

for index in 0, 8, 2:
    try:
        print(colors[index])
    except IndexError as err:
        print(err)

airports = {
    'RDU': 'Raleigh-Durham',
    'SEA': 'Sea-Tac',
    'BWI': 'Baltimore-Washington',
    'DCA': 'Washington Reagan',
}

for code in 'RDU', 'BWI', 'LAX':
    try:
        print(airports[code])
    except KeyError as err:
        print(err)

x = 22.9

values = 0, 5.1, 8.9, 0.0, 4.3, 'ABC', 1.7

for v in values:
    try:
        result = x / v
    except (TypeError, ZeroDivisionError) as err:   # err = ZeroDivisionError("Message")
        print(err)
    except ValueError as err:
        print(err)
    except Exception as err:  # trap all types
        print(err)
    else:
        print(result)
    finally:
        pass