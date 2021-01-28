fruits = ['apple', 'banana', 'kiwi', 'peach', 'lime', 'lemon', 'mango', 'date', 
'elderberry', 'watermelon', 'pomegranate']

# WRITING TO A TEXT FILE

# fruits_out = open("fruits.txt", "w")
with open("fruits.txt", "w") as fruits_out:  # open in write mode and get file object
    for fruit in fruits:   # for each fruit
        fruits_out.write(fruit + '\n')   # write fruit and newline to file
    # fruits_out.close() 

# READING FROM TEXT FILES
with open("fruits.txt", "r") as fruit_in:
    for raw_line in fruit_in:  # file object is GENERATOR of lines in file
        #  print(repr(raw_line))
        line = raw_line.rstrip()
        print(line)
print('-' * 60)


with open("fruits.txt") as fruit_in:
    contents = fruit_in.read() # read entire file into 1 string
    print("RAW")
    print(repr(contents))
    print("NORMAL")
    print(contents)
print('-' * 60)

with open("fruits.txt") as fruit_in:
    all_lines_with_nl = fruit_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open("fruits.txt") as fruit_in:
    all_lines_without_nl = fruit_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)
