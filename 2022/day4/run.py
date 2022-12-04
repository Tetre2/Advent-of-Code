f = open("input.txt", "r")
data = f.readlines()

def generate_range(interval):
    start, end = interval.split("-")
    start = int(start)
    end = int(end)
    #print(interval, start, end)
    return set(range(start, end + 1))

amount = 0

for schedule in data:
    worker1, worker2 = schedule.split(",")
    set1 = generate_range(worker1)
    set2 = generate_range(worker2)

    #print(set1, set2, set1.intersection(set2))

    # Part 1
    #if set1.issubset(set2) or set2.issubset(set1):
    #    amount += 1
    # Part 2
    if any(set1.intersection(set2)):
        amount += 1

print(amount)


