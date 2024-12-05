import re

f = open('input.txt', 'r')
data = f.read().split("\n")

t1 = open('part1Sample.txt', 'r')
testdata1 = t1.read().split("\n")

t2 = open('part2Sample.txt', 'r')
testdata2 = t2.read().split("\n")


def isValid(arr):
    decreasing = arr[0] - arr[1] > 0
    for i in range(len(arr)-1):
        if decreasing and arr[i] - arr[i + 1] not in [1, 2, 3]: return 0
        elif not decreasing and arr[i] - arr[i + 1] not in [-1, -2, -3]: return 0
    return 1

def part1():
    safe = 0
    for line in data:
        line = list(map(int, line.split(" ")))
        safe += isValid(line)
    return safe


def part2():
    safe = 0
    for line in data:
        line = list(map(int, line.split(" ")))
        
        if isValid(line) < 1:
            for i in range(len(line)):
                tmp = line.copy()
                tmp.pop(i)
                if isValid(tmp) == 1:
                    safe += 1
                    break
        else:
            safe += 1
            
    return safe


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
