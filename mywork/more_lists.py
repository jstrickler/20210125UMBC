cities = list()

cities.append("Glen Burnie")
cities.append("Pasadena")
cities.append("Columbia")
print(cities)
print(cities[0], cities[2], cities[-1])
cities.insert(0, "Laurel")
cities.insert(3, "Aberdeen")
print(cities)
cities[2] = "Silver Spring"
print(cities)

for city in cities:
    print(city.upper())


