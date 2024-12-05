import re

f = open('input.txt', 'r')
data = f.read().split("\n\n")

t1 = open('part1Sample.txt', 'r')
testdata1 = t1.read().split("\n\n")

t2 = open('part2Sample.txt', 'r')
testdata2 = t2.read().split("\n\n")


rules = dict()
for rule in data[0].split("\n"):
    left, right = rule.split("|")
    rules[right] = rules.get(right, list()) + [left]

def isBad(pages):
    for index, page in enumerate(pages[:-1]):
        if set(rules.get(page, list())) & set(pages[index+1:]):
            return True
    return False

def part1():
    sum = 0
    for line in data[1].split("\n"):
        pages = line.split(",")
        if not isBad(pages):
            sum += int(pages[len(pages)//2])
    return sum
 
def correctOrder(pages:list):
    if not isBad(pages):
        return pages
    for index, page in enumerate(pages[:-1]):
        if set(rules.get(page, list())) & set(pages[index+1:]):
            tmp = pages.index((set(rules.get(page, list())) & set(pages[index+1:])).pop())
            pages[tmp], pages[index] = pages[index], pages[tmp]
            return correctOrder(pages)

def part2():
    sum = 0
    for line in data[1].split("\n"):
        pages = line.split(",")
        if isBad(pages):
            corrected = correctOrder(pages)
            sum += int(corrected[len(corrected)//2])
    return sum


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
