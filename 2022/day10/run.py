f = open('input.txt', 'r')
data = f.readlines()

cycle = 0
signal_sum = 0
reg_x = 1
# Part 1
# def check_signal_strength():
#     global signal_sum
#     if (cycle - 20) % 40 == 0:
#         signal_sum += (reg_x * cycle)

# for instructiuon in data:
#     cycle += 1
#     check_signal_strength()

#     if instructiuon[0] == 'a':
#         cycle += 1
#         check_signal_strength()
#         val = int(instructiuon.split(" ")[1])
#         reg_x += val

# print(signal_sum)
    

# Part 2
instructiuon = None
screen = []
for _ in range(6):
    screen.append(list("." * 40))
row = ""
y = 0
pixel = 0

def paint():
    global row
    global pixel
    global y
    
    print(cycle, pixel, reg_x)
    
    if pixel == reg_x - 1 or pixel == reg_x or pixel == reg_x + 1:
        row = row + "#"
        screen[y][pixel] = "#"
    else:
        row = row + "."
        screen[y][pixel] = "."
    
    print("".join(screen[y]))
    s = ""
    for i in range(40):
        if i == reg_x - 1 or i == reg_x or i == reg_x + 1:
            s = s + "$"
        else:
            s = s + "-"
    print(s)
    
    pixel += 1

    if pixel % 40 == 0:
        print(row)
        row = ""
        y += 1
        pixel = 0


while cycle < 240:
    cycle += 1
    paint()

    if instructiuon != None:
        val = int(instructiuon.split(" ")[1])
        reg_x += val
        instructiuon = None
    else:
        instructiuon = data.pop(0)
        if instructiuon[0] == 'n':
            instructiuon = None


for i in screen:
    print("".join(i))



