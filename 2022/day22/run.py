from copy import deepcopy


f = open('/home/tetre/workspace/Advent-of-Code/2022/day22/test.txt', 'r')
data = f.readlines()


board = []
instructions = None
current_pos = (0, 0)
facing = 'R'

for i, row in enumerate(data):
    row = row.strip('\n')
    if row == '':
        instructions = list(data[i + 1].strip('\n'))
        break
    else:
        board.append(list(row))

width = len(board[0])
height = len(board)

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] <= width - 1 and pos[1] >= 0 and pos[1] <= height - 1

#def move(pos: tuple(int, int)) -> tuple(int, int):
def move(pos): 
    next_pos = None
    # print(f"got {pos}")
    if facing == 'R':
        next_pos = ((pos[0] + 1) % width, pos[1])    
    elif facing == 'L':
        next_pos = ((pos[0] + width - 1) % width, pos[1])
    elif facing == 'D':
        next_pos = (pos[0], (pos[1] + 1) % height)
    elif facing == 'U':
        next_pos = (pos[0], (pos[1] + height - 1) % height)
        
    # print(f"next is {next_pos}, hw: {height, width}")
    # print(board[199][50])

    if board[next_pos[1]][next_pos[0]] == '#':
        # print(f"hit a wall {next_pos}")
        return False
    elif board[next_pos[1]][next_pos[0]] == ' ':
        # print(f"recur {next_pos}")
        return move(next_pos)
    
    # print(f"returning {next_pos}")
    board[next_pos[1]][next_pos[0]] = "o"
    return next_pos


def turn(dir:str):
    global facing
    next_dir = ["U", "R", "D", "L"]
    # print(next_dir.index(facing))
    if dir == "R":
        facing = next_dir[(next_dir.index(facing) + 1) % 4]
    else:
        facing = next_dir[(next_dir.index(facing) + 3) % 4]
    # print(f"now facing {facing}")






ins = []
numb = ""
for char in instructions:
    if char.isdigit():
        numb += char
    else:
        if numb != '':
            ins.append(int(numb))
            numb = ""
            ins.append(char)
if numb != "":
    ins.append(int(numb))

instructions = ins

for ins in instructions:
    # print(ins, facing, current_pos)
    if isinstance(ins, int):
        for i in range(ins):
            m = move(current_pos)
            if isinstance(m, tuple):
                current_pos = m
    else:
        turn(ins)
    
    # for i in board:
    #     print("".join(i))


res = (1000 * (current_pos[1] + 1)) + (4 * (current_pos[0] + 1))


print(res, facing)
    
tmp = deepcopy(board)
    
tmp = 2

print(board)

f = open("mask.txt", "a")
for i in tmp:
    f.write("".join(i) + '\n')


