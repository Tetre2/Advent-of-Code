f = open('input.txt', 'r')
data = f.readlines()

instructiuon = None
cycle = 0
signal_sum = 0
reg_x = 1
# Part 1
def check_signal_strength():
    global signal_sum
    if (cycle - 20) % 40 == 0:
        signal_sum += (reg_x * cycle)

# Part 2
row = ""
pixel = 0
def paint():
    global row
    global pixel

    if pixel == reg_x - 1 or pixel == reg_x or pixel == reg_x + 1:
        row = row + "#"
    else:
        row = row + "."

    pixel += 1
    if pixel % 40 == 0:
        print(row)
        row = ""
        pixel = 0

while cycle < 240:
    cycle += 1
    #check_signal_strength()
    paint()

    if instructiuon != None:
        val = int(instructiuon.split(" ")[1])
        reg_x += val
        instructiuon = None
    else:
        instructiuon = data.pop(0)
        if instructiuon[0] == 'n':
            instructiuon = None


#print(signal_sum)