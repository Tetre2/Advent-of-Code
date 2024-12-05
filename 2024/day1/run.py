import re
from collections import Counter

f = open('input.txt', 'r')
data = f.read()

t1 = open('part1Sample.txt', 'r')
testdata1 = t1.read()

t2 = open('part2Sample.txt', 'r')
testdata2 = t2.read()

lefts = []
rights = []

for left, right in re.findall(r'(\d+)   (\d+)', data):
    lefts.append(int(left))
    rights.append(int(right))

lefts = sorted(lefts)
rights = sorted(rights)

def part1():
    return sum(list(map(lambda x: abs(x[0] - x[1]), zip(lefts, rights))))

def part2():
    global rights
    rights = Counter(rights)
    return sum(list(map(lambda x: rights.get(x, 0) * x, lefts)))


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
