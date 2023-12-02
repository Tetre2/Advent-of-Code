f = open('input.txt', 'r')
data = f.readlines()

t = open('test1star.txt', 'r')
testdata = t.readlines()

def getAmountOfColor(cubes, color):
    for i in cubes:
        amount, cubeColor = i.split(" ")
        if cubeColor == color:
            return int(amount)
    return 0

results = 0

for line in data:
    line = line[:-1]
    gameNumb, runs = line.split(": ")

    reds = 1
    blues = 1
    greens = 1
    games = runs.split("; ")
    for game in games:
        cubes = game.split(", ")
        if getAmountOfColor(cubes, "red") > reds:
            reds = getAmountOfColor(cubes, "red")
        if getAmountOfColor(cubes, "green") > greens:
            greens = getAmountOfColor(cubes, "green")
        if getAmountOfColor(cubes, "blue") > blues:
            blues = getAmountOfColor(cubes, "blue")
    results += (reds * blues * greens)

print(results)
