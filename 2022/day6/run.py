f = open('input.txt', 'r')
data = f.readlines()[0]

def is_unique(arr):
    return len(set(arr)) == len(arr)

arr = list(data[:14]) # Change size to 4 or 14 
pointer = 0
index = len(arr)

while not is_unique(arr):
    arr[pointer] = data[index]
    pointer = (pointer + 1) % len(arr)
    index += 1

print(index)


