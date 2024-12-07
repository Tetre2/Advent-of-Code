import re

f = open('input.txt', 'r')
data = f.read().split("\n")

t1 = open('part1Sample.txt', 'r')
testdata1 = t1.read().split("\n")

t2 = open('part2Sample.txt', 'r')
testdata2 = t2.read().split("\n")

def part1(data):
    total = []
    for line in data:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split(" ")))
        result = [numbers[0]]
        for numb in numbers[1:]:
            muls = [n * numb for n in result]
            adds = [n + numb for n in result]
            result = muls + adds
        if target in result:
            total.append(target)
    return sum(total)


def part2(data):
    total = []
    for line in data:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split(" ")))
        result = [numbers[0]]
        for numb in numbers[1:]:
            muls = [n * numb for n in result]
            adds = [n + numb for n in result]
            cons = [int(str(n) + str(numb)) for n in result]
            result = muls + adds + cons
        if target in result:
            total.append(target)
    return sum(total)

print(f'Part1: {part1(data)}')
print(f'Part2: {part2(data)}')