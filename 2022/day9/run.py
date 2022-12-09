f = open('input.txt', 'r')
data = f.readlines()

size = 1000
head = (size*size)//2 # in the middle
tail = (size*size)//2

possitions = []

def move(dir):
    global head
    global tail
    new_head = head
    if dir == "U":
        new_head -= size
    
    if dir == "D":
        new_head += size

    if dir == "L":
        new_head -= 1
    
    if dir == "R":
        new_head += 1
            
    #                       Top row                                        Middle row                                           Bottom row
    if not ((new_head >= tail - size - 1 and new_head <= tail - size + 1) or (new_head >= tail - 1 and new_head <= tail + 1) or (new_head >= tail + size - 1 and new_head <= tail + size + 1)):
        tail = head
        possitions.append(tail)

    head = new_head

for row in data:
    row = row.strip("\n")
    dir, amount = row.split(" ")
    for i in range(int(amount)):
        move(dir)

print(len(set(possitions)))