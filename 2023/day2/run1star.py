f = open('input.txt', 'r')
data = f.readlines()

t = open('test1star.txt', 'r')
testdata = t.readlines()

def getAmountOfColor(cubes, color):
    for i in cubes:
        amount, cubeColor = i.split(" ")
        if cubeColor == color:
            return amount
    return 0

results = 0

for line in data:
    line = line[:-1]
    gameNumb, runs = line.split(": ")
    gameNumb = gameNumb.split(" ")[1]

    validGame = True
    games = runs.split("; ")
    for game in games:
        cubes = game.split(", ")
        reds = getAmountOfColor(cubes, "red")
        greens = getAmountOfColor(cubes, "green")
        blues = getAmountOfColor(cubes, "blue")
        if int(reds) > 12 or int(greens) > 13 or int(blues) > 14:
            validGame = False
    
    if validGame:
        results += int(gameNumb)

print(results)
