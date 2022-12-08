f = open('test.txt', 'r')
data = f.readlines()

numbers = []

for row in data:
    row = row.strip('\n')
    arr = list(row)
    for i, numb in enumerate(arr):
        arr[i] = [int(numb), False]
    numbers.append(arr)

size = (len(numbers[0]), len(numbers))

amount = 0
# Part 1
# def check_line(arr):
#     amount = 0
#     front = -1
#     end = -1
#     for i in range(len(arr)):
#         if front < arr[i][0]:
#             front = arr[i][0]
#             if not arr[i][1]:
#                 amount += 1
#                 arr[i][1] = True
        
#         if end < arr[len(arr) - 1 - i][0]:
#             end = arr[len(arr) - 1 - i][0]
#             if not arr[len(arr) - 1 - i][1]:
#                 amount += 1
#                 arr[len(arr) - 1 - i][1] = True
        
#     return amount

# for row in numbers:
#     amount += check_line(row)

# for col in range(len(numbers)):
#     column = []
#     for row in range(len(numbers)):
#         column.append(numbers[row][col])
#     amount += check_line(column)

# print(amount)

# Part 2

def get_score(y, x):
    down_amount = 0
    up_amount = 0
    right_amount = 0
    left_amount = 0
    height = numbers[y][x][0]
    numbers[y][x][1] = True
    down_stop = False
    up_stop = False
    right_stop = False
    left_stop = False
    for i in range(len(numbers) - 1):
        i += 1
        # Down
        if y + i < len(numbers) and not down_stop:
            down_amount += 1
            if height <= numbers[y + i][x][0]:
                down_stop = True
                
        # Up
        if y - i > -1 and not up_stop:
            up_amount += 1
            if height <= numbers[y - i][x][0]:
                up_stop = True

        # Right
        if x + i < len(numbers) and not right_stop:
            right_amount += 1
            if height <= numbers[y][x + i][0]:
                right_stop = True

        # Left
        if x - i > -1 and not left_stop:
            left_amount += 1
            if height <= numbers[y][x - i][0]:
                left_stop = True
            
    return down_amount * up_amount * right_amount * left_amount

for row in range(len(numbers)):
    for col in range(len(numbers)):
        score = get_score(row, col)
        if score > amount:
            amount = score

print(amount)

# print(numbers[1])

# for i in numbers:
#     print(i)
