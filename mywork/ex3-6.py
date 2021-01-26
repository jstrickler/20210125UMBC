raw_start = input("Enter starting number: ")
raw_stop = input("Enter stopping number: ")
raw_step = input("Enter step: ")

start = int(raw_start)
stop = int(raw_stop)
step = int(raw_step)

for n in range(start, stop + 1, step):
    print(n, end=" ")
print("\n")
