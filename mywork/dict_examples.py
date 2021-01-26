#!/usr/bin/env python3

d1 = dict()
print(d1)
d2 = {'a': 5, 'm': 6, 'j': 2}
print(d2)
d3 = {}
print(d3)
d4 = dict(name="Bob", city="Tampa", game="Settlers of Catan")
print(d4)

airports = {
    'BWI': "Thurgood Marshall",
    'DCA': "Reagan",
    'IAD': "Dulles",
    'RIC': "Richmond",
}
print(airports['BWI'])
print(airports.get('BWI'))
print(airports.get('LAX'))
print(airports.get('LAX', 'UNKNOWN'))

airports['PIT'] = "Pittsburgh"
airports['SEA'] = 'Seattle/Tacoma'

print(airports)

airports['SEA'] = "Sea-Tac"
print(airports)

del airports['RIC']  #  x = airports.pop('RIC')
print(airports, '\n')

for abbr, name in airports.items():
    print(abbr, name)
print()

print(airports.keys())
print(airports.values())

print(len(airports))






