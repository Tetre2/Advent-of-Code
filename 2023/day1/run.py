from re import split
f = open('input.txt', 'r')
#f = open('test.txt', 'r')
data = f.readlines()

result = 0

for line in data:
    s = "".join(split((r'\D'), line))
    result += int(s[0] + s[-1])

print(result)