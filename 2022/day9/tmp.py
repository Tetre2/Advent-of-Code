f = open('input.txt', 'r')
data = f.readlines()

size = 1000
rope_knots = 10
knots = []
for _ in range(rope_knots):
    knots.append([size//2, size//2])
board = []
for _ in range(size):
    board.append(list(["."] * size))


possitions = []

def show():
    for i in board:
        print("".join(i))

def move(dir):
    global knots
    if dir == "U":
        knots[0][1] -= 1
    
    if dir == "D":
        knots[0][1] += 1

    if dir == "L":
        knots[0][0] -= 1
    
    if dir == "R":
        knots[0][0] += 1
    
    for i in range(rope_knots - 1):
        i += 1

        y_dist = knots[i-1][1] - knots[i][1]
        x_dist = knots[i-1][0] - knots[i][0]

        if y_dist < -1 or y_dist > 1 or x_dist < -1 or x_dist > 1:
            if not y_dist == 0: knots[i][1] += 1 * abs(y_dist)//y_dist
            if not x_dist == 0: knots[i][0] += 1 * abs(x_dist)//x_dist
            
        if i == rope_knots - 1:
            possitions.append((knots[i][0],knots[i][1]))

    for i, k in enumerate(knots):
        board[k[1]][k[0]] = str(i)


for row in data:
    row = row.strip("\n")
    dir, amount = row.split(" ")
    for i in range(int(amount)):
       move(dir)

print(len(set(possitions)))


