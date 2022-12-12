from dataclasses import dataclass
f = open('input.txt', 'r')
data = f.readlines()

@dataclass
class monkey:
    items: list
    opr: None
    test: int
    endpoint_true: int
    endpoint_false: int
    inspected = 0

mod = 13 * 3 * 7 * 2 * 19 * 5 * 11 * 17
monkeys = [monkey([89, 73, 66, 57, 64, 80], lambda x: x*3, 13, 6, 2), 
monkey([83, 78, 81, 55, 81, 59, 69], lambda x: x+1, 3, 7, 4), 
monkey([76, 91, 58, 85], lambda x: x*13, 7, 1, 4), 
monkey([71, 72, 74, 76, 68], lambda x: x*x, 2, 6, 0), 
monkey([98, 85, 84], lambda x: x+7, 19, 5, 7), 
monkey([78], lambda x: x+8, 5, 3, 0), 
monkey([86, 70, 60, 88, 88, 78, 74, 83], lambda x: x+4, 11, 1, 2), 
monkey([81, 58], lambda x: x+5, 17, 3, 5)]

# mod = 23 * 19 * 13 * 17
# monkeys = [monkey([79, 98], lambda x: x*19, 23, 2, 3), 
# monkey([54, 65, 75, 74], lambda x: x+6, 19, 2, 0), 
# monkey([79, 60, 97], lambda x: x*x, 13, 1, 3), 
# monkey([74], lambda x: x+3, 17, 0, 1)]

for round in range(10000):
    for i, m in enumerate(monkeys):
        #print(f"monkey {i}:")
        for _ in range(len(m.items)):
            item = m.items.pop(0)
            m.inspected += 1
            #print(f"    Monkey inspects an item with a worry level of {item}.")
            item = m.opr(item)
            #print(f"\tWorry level is multiplied by {m.opr} to {item}.")
            
            #item = item // 3   # Part 1
            item = item % mod   # Part 2
            
            #print(f"\tMonkey gets bored with item. Worry level is divided by 3 to {item}.")
            if item % m.test == 0:
                #print(f"\tCurrent worry level is divisible by {m.test}.\n\tItem with worry level {item} is thrown to monkey {m.endpoint_false}.")
                monkeys[m.endpoint_true].items.append(item)
            else:
                #print(f"\tCurrent worry level is not divisible by {m.test}.\n\tItem with worry level {item} is thrown to monkey {m.endpoint_false}.")
                monkeys[m.endpoint_false].items.append(item)      

inspects = []
for i in monkeys:
    inspects.append(i.inspected)

inspects.sort(reverse=True)
print(inspects)
print(inspects[0] * inspects[1])



