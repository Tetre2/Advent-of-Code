import re

f = open('input.txt', 'r')
data = f.read().split("\n")

t1 = open('part1Sample.txt', 'r')
testdata1 = t1.read().split("\n")

t2 = open('part2Sample.txt', 'r')
testdata2 = t2.read().split("\n")


def func(x, y):
    xmases = 0
    if data[y][x] == "X":
        if x + 3 < len(data) and data[y][x + 1] == "M" and data[y][x + 2] == "A" and data[y][x + 3] == "S":
            xmases += 1
        if x - 3 >= 0 and data[y][x - 1] == "M" and data[y][x - 2] == "A" and data[y][x - 3] == "S":
            xmases += 1
        if y + 3 < len(data) and data[y + 1][x] == "M" and data[y + 2][x] == "A" and data[y + 3][x] == "S":
            xmases += 1
        if y - 3 >= 0 and data[y - 1][x] == "M" and data[y - 2][x] == "A" and data[y - 3][x] == "S":
            xmases += 1
        if x + 3 < len(data) and y + 3 < len(data) and data[y + 1][x + 1] == "M" and data[y + 2][x + 2] == "A" and data[y + 3][x + 3] == "S":
            xmases += 1
        if x - 3 >= 0 and y - 3 >= 0 and data[y - 1][x - 1] == "M" and data[y - 2][x - 2] == "A" and data[y - 3][x - 3] == "S":
            xmases += 1
        if x - 3 >= 0 and y + 3 < len(data) and data[y + 1][x - 1] == "M" and data[y + 2][x - 2] == "A" and data[y + 3][x - 3] == "S":
            xmases += 1
        if x + 3 < len(data) and y - 3 >= 0 and data[y - 1][x + 1] == "M" and data[y - 2][x + 2] == "A" and data[y - 3][x + 3] == "S":
            xmases += 1
    return xmases

def part1(data):
    sum = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            res = func(x, y)
            sum += res
    return sum

def func2(x, y):
    if data[y][x] == "A" and 0 < x < len(data)-1 and 0 < y < len(data)-1:
        if ((data[y - 1][x - 1] == "M" and data[y + 1][x + 1] == "S") or (data[y - 1][x - 1] == "S" and data[y + 1][x + 1] == "M")) and ((data[y + 1][x - 1] == "S" and data[y - 1][x + 1] == "M") or (data[y + 1][x - 1] == "M" and data[y - 1][x + 1] == "S")):
            return 1
    return 0

def part2(data):
    sum = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            res = func2(x, y)
            sum += res
    return sum


print(f'Part1: {part1(data)}')
print(f'Part2: {part2(data)}')
