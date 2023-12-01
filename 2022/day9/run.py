f = open('test.txt', 'r')
data = f.readlines()

size = 1000
head = (size*size)//2 # in the middle
tail = (size*size)//2

rope_knots = 10
knots = []
for _ in range(rope_knots):
    knots.append(size//2)

possitions = []

def move(dir):
    global knots

    if dir == "U":
        knots[0] -= size
    
    if dir == "D":
        knots[0] += size

    if dir == "L":
        knots[0] -= 1
    
    if dir == "R":
        knots[0] += 1

    for i, knot in enumerate(knots):
        if i == 0: continue
        
        #                       Top row                                        Middle row                                           Bottom row
        if not ((knots[i-1] >= knot - size - 1 and knots[i-1] <= knot - size + 1) or (knots[i-1] >= knot - 1 and knots[i-1] <= knot + 1) or (knots[i-1] >= knot + size - 1 and knots[i-1] <= knot + size + 1)):
            y_change = (knots[i-1] - knot + 1) //size
            x_change = (knots[i-1] - knot + 1) % size
            if not y_change == 0: knot += size * (abs(y_change)//y_change)
            if not x_change == 0: knot += abs(x_change)//x_change
            
            if i == rope_knots - 1: 
                possitions.append(knot)


for row in data:
    row = row.strip("\n")
    dir, amount = row.split(" ")
    for i in range(int(amount)):
        move(dir)

print(len(set(possitions)))