
f = open("day1.txt", "r")
data = f.readlines()

cal = []
numb = 0
while len(data) != 0:
    item = data.pop(0)
    if item == '\n':
        cal.append(numb)
        numb = 0
        continue
    numb += int(item)

sum = 0
for _ in range(3):
    m = max(cal)
    sum += m
    cal.remove(m)
print(sum)
