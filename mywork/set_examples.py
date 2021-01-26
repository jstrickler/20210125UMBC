
colors1 = ['red', 'blue', 'green', 'blue', 'purple', 'orange', 'blue', 'yellow']
colors2 = ['green', 'green', 'purple', 'orange', 'pink', 'cyan', 'green']

set1 = set(colors1)
set2 = set(colors2)

set2.add('brown')
set2.add('black')
set1.add('white')

for i in range(1000000):
    set1.add("chartreuse")

print("set1:", set1)
print("set2:", set2)

print("Both:", set1 & set2)
print("Only one:", set1 ^ set2)
print("Combined:", set1 | set2)
print("Just set1:", set1 - set2)
print("Just set2:", set2 - set1)

for color in 'yellow', 'taupe', 'burnt umber':
    set1.discard(color)
    set2.discard(color)

print("set1:", set1)
print("set2:", set2)




