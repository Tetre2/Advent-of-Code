f = open('input.txt', 'r')
data = f.readlines()

#create the table
tmp = []
for row in data:
    if row == '\n':
        break
    tmp.append(row)

# calc the number of required stacks
numb_of_stacks = int(tmp[-1:][0][-3:][0])
stacks = []

#because lists are weard in python append {numb_of_stacks} 
for _ in range(numb_of_stacks):
    stacks.append([])

# remove the teble from the original input
for i in range(len(tmp) + 1):
    data.pop(0) 

# insert the data into the stacks
for row in tmp[:-1]:
    for stack in range(numb_of_stacks):
        char = row[(stack*4) + 1]
        if char != ' ':
            stacks[stack].insert(0, char)


for move in data:
    steps = move.split(" ")
    amount = int(steps[1])
    origin = int(steps[3])
    dest = int(steps[5])
    intermideate = []
    for i in range(amount):
        # Part 1
        # stacks[dest - 1].append(stacks[origin - 1].pop())

        # Part 2
        intermideate.append(stacks[origin - 1].pop())
    for i in range(amount):
        stacks[dest - 1].append(intermideate.pop())

a = []
for i in stacks:
    if len(i) > 0:
        a.append(i.pop())

print(a)
