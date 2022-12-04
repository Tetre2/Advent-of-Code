f = open("day3.txt", "r")
data = f.readlines()

def contains(list):
    l = []
    for word in list:
        chars = set()
        for char in word:
            chars.add(char)
        l.append(chars)
        
    result = l[0]
    for sets in range(1, len(l)):
        result.intersection_update(l[sets])

    print(result)
    return result.pop()

def char_to_int(char):
    val = ord(char)
    val = val - 96
    if val < 0:
        val += 26 + 32
    return val

score = 0

    # First Problem
    
# for backpack in data:
#     s = backpack
#     s = s.split('\n')[0]

#     middle = int(len(s)/2)
#     first = s[:middle]
#     second = s[middle:]
#     score += char_to_int(contains([first, second]))



    # Second Problem
def get_backpack(index):
    res = []
    for i in range(3):
        s = data[index + i]
        s = s.split('\n')[0]
        res.append(s)
    print(res)
    return res


for index in range(int(len(data)/3)):
    backpacks = get_backpack(index * 3)
    score += char_to_int(contains(backpacks))

print(score)

