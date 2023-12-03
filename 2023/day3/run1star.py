from re import sub

f = open('input.txt', 'r')
data = f.readlines()

t = open('test1star.txt', 'r')
testdata = t.readlines()

results = 0
characters = set(sub(r'\d|\.', "", "".join(data)))

output = ""

def containsAny(string:str):
    for char in characters:
        if string.count(char) > 0:
            return True
    return False

for row, line in enumerate(testdata):
    startIndex = 0
    endIndex = 0
    isNumb = False
    numb = ""
    for index, char in enumerate(line):
        if char != "." and char not in characters:
            if not isNumb:
                startIndex = index
            isNumb = True
            numb += char
        else:
            if isNumb:
                endIndex = index + 1
                isNumb = False
                left = False
                right = False
                appended = False
                if startIndex > 0:
                    left = True
                if endIndex < len(testdata) - 1:
                    right = True

                if row > 0:
                    if containsAny(testdata[row - 1][startIndex - 1 if left else startIndex : endIndex + 1 if right else endIndex]):
                        results += int(numb)
                        appended = True
                if not appended:
                    if containsAny(testdata[row][startIndex - 1 if left else startIndex : endIndex + 1 if right else endIndex]):
                        results += int(numb)
                        appended = True
                if row < len(testdata) - 1 and not appended:
                    if containsAny(testdata[row + 1][startIndex - 1 if left else startIndex : endIndex + 1 if right else endIndex]):
                        results += int(numb)
                        appended = True

                if appended:
                    for i in numb:
                        output += "_"
                else:
                    output += numb
                numb = ""
            output += char

    output += "\n"

print(results)

print(output)

