from re import split
f = open('input.txt', 'r')
#f = open('test.txt', 'r')
data = f.readlines()

result = 0

for line in data:
    s = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
    s = "".join(split((r'\D'), s))
    i = int(s[0] + s[-1])
    result += int(s[0] + s[-1])

print(result)