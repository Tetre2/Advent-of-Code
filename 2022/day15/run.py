f = open('input.txt', 'r')
data = f.readlines()

sb_pairs = []
for line in data:
    _, sx, sy, bx, by = line.split("=")
    sx = int(sx.split(",")[0])
    sy = int(sy.split(":")[0])
    bx = int(bx.split(",")[0])
    by = int(by)
    sb_pairs.append([sx, sy, bx, by])

minelement = 0
size = 0
for sb in sb_pairs:
    if min(sb) < minelement:
        minelement = min(sb)

    if max(sb) > size:
        size = max(sb)

minelement = minelement * -1 
size += minelement + 1

for i, sb in enumerate(sb_pairs):
    sb_pairs[i] = [sb[0] + minelement, sb[1] + minelement, sb[2] + minelement, sb[3] + minelement]

# print(sb_pairs)
# print(minelement, size)

board = []

for _ in range(size):
    board.append(["."] * size)

for sb in sb_pairs:
    board[sb[1]][sb[0]] = "S"
    board[sb[3]][sb[2]] = "B"

# checked = []

# def check_possition(x, y):
#     global checked
#     global size
#     neighbours = []
#     if x >= 0 and x <= size - 1 and y >= 0 and y <= size - 1:
            
#             if board[y][x] == "B":
#                 print(f"closes becon at: x={x}, y={y}")
#                 return True
#             if board[y][x] != "S":
#                 board[y][x] = "#"
#                 checked.append((x, y))

#             if x > 0 and not((x - 1, y) in checked):
#                 neighbours.append((x - 1, y))
#             if x < size - 1 and not((x + 1, y) in checked):
#                 neighbours.append((x + 1, y))

#             if y > 0 and not((x, y - 1) in checked):
#                 neighbours.append((x, y - 1))
#             if y < size - 1 and not((x, y + 1) in checked):
#                 neighbours.append((x, y + 1))
#     return neighbours
    

def get_closest(x, y):
    global size
    checked = []
    current = [[x, y]]
    becon_found = False
    while not becon_found:
        check_next = []
        for pos in current:
            if pos[0] >= 0 and pos[0] <= size - 1 and pos[1] >= 0 and pos[1] <= size - 1:
                    
                if board[pos[1]][pos[0]] == "B":
                    print(f"closes becon at: x={pos[0]}, y={pos[1]}")
                    becon_found = True
                    continue
                if board[pos[1]][pos[0]] != "S":
                    board[pos[1]][pos[0]] = "#"
                    checked.append((pos[0], pos[1]))

                if pos[0] > 0 and not((pos[0] - 1, pos[1]) in checked):
                    check_next.append((pos[0] - 1, pos[1]))
                if pos[0] < size - 1 and not((pos[0] + 1, pos[1]) in checked):
                    check_next.append((pos[0] + 1, pos[1]))

                if pos[1] > 0 and not((pos[0], pos[1] - 1) in checked):
                    check_next.append((pos[0], pos[1] - 1))
                if pos[1] < size - 1 and not((pos[0], pos[1] + 1) in checked):
                    check_next.append((pos[0], pos[1] + 1))

        #print(f"next {len(check_next)}")
        #print(f"checked {len(checked)}")
        if len(check_next) == 0:
            break
        current = set(check_next)

        
for i in sb_pairs:
    print(f"checking: {i}")
    get_closest(i[0], i[1])
#     row = 0
#     for i in board:
#         i = "".join(i)
#         print(f"{row}:\t{i}")
#         row += 1

print(board[12].count("#"))

# get_closest(16, 19)
# row = 0
# for i in board:
#     i = "".join(i)
#     print(f"{row}:\t{i}")
#     row += 1
