
f = open("ady2.txt", "r")
data = f.readlines()

# A = Rock      = 1         
# B = Paper     = 2         
# C = Sciossors = 3    

# X = Rock      = 1     X = Loss
# Y = Paper     = 2     Y = Draw
# Z = Scissors  = 3     Z = Win

# Win = 6
# Darw = 3
# Loss = 0

# B Z


def convert(letter):
    if letter == "A" or letter == "X":
        return 1
    if letter == "B" or letter == "Y":
        return 2
    if letter == "C" or letter == "Z":
        return 3

# Op     Me
# Rock v Paper      = Paper     1 - 2 = -1  Win
# Paper v Rock      = Paper     2 - 1 = 1   Loss

# Scissors v Rock   = Rock      3 - 1 = 2  Win
# Rock v Scissors   = Rock      1 - 3 = -2  Loss

# Paper v Scissors  = Scissors  2 - 3 = -1   Win
# Scissors v Paper  = Scissors  3 - 2 = 1   Loss
def calc_score(op, me):
    res = op - me
    print(op, me, res)
    if res == 0:
        return 3 + me
    elif res == -1 or res == 2: # Win
        return 6 + me
    else:
        return me
    
score = 0
for i in data:
    op = convert(i[0])
    me = convert(i[2])

    #First challange
    #score += calc_score(op, me) 

    # Second challange
    move = 1
    if me == 1: # Lose
        move = ((op + 2)  % 3)
        if move < 1:
            move += 3

    elif me == 2: # Draw
        move = op
        
    else:
        move = (op % 3) + 1

    score += calc_score(op, move)

print(score)
