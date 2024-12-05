import re

f = open('input.txt', 'r')
data = f.read()

t1 = open('part1Sample.txt', 'r')
testdata1 = t1.read()

t2 = open('part2Sample.txt', 'r')
testdata2 = t2.read()

def func(instruction):
    numb1, numb2 = re.findall(r'\d+', instruction)
    return int(numb1) * int(numb2)


def part1(data):
    results = 0
    instructions = re.findall(r'mul\(\d+,\d+\)', data)
    results += sum(map(func, instructions))

    return results

def part2(data):
    results = 0
    do = True
    instructions = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', data)
    for inst in instructions:
        if inst == "do()":
            do = True
            continue
        elif inst == "don\'t()":
            do = False
            continue
        if do:
            results += func(inst)
    return results

print(f'Part1: {part1(data)}')
print(f'Part2: {part2(data)}')