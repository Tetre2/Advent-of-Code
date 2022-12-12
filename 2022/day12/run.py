from dataclasses import dataclass

f = open('input.txt', 'r')
data = f.readlines()

for i, row in enumerate(data):
    data[i] = row.strip('\n')

@dataclass
class node:
    neighbours: list
    height: str
    distance = 100000
    hops = 0

    def show(self) -> str:
        s = "["
        for i in self.neighbours:
            s = s + "" + i.height
        
        return f"{s}], {self.height}, {self.distance}, {self.hops}"

def char_to_int(char):
    if char == "S":
        return 0
    if (char == "E"):
        return 27
    val = ord(char)
    val = val - 96
    if val < 0:
        val += 26 + 32
    return val

nodes = []
all_nodes = []

for row in data:
    nodes.append([None] * len(row))

for y, row in enumerate(data):
    for x, char in enumerate(list(row)):
        n = node([], char)
        nodes[y][x] = n
        all_nodes.append(n)

for y, row in enumerate(data):
    for x, char in enumerate(list(row)):
        #print(y, x)
        if x > 0 and char_to_int(nodes[y][x].height) >= char_to_int(nodes[y][x - 1].height) - 1:
            nodes[y][x].neighbours.append(nodes[y][x - 1])
            
        if x < len(row) - 1 and char_to_int(nodes[y][x].height) >= char_to_int(nodes[y][x + 1].height) - 1:
            nodes[y][x].neighbours.append(nodes[y][x + 1])
            

        if y > 0 and char_to_int(nodes[y][x].height) >= char_to_int(nodes[y - 1][x].height) - 1:
            nodes[y][x].neighbours.append(nodes[y - 1][x])
            
        if y < len(data) - 1 and char_to_int(nodes[y][x].height) >= char_to_int(nodes[y + 1][x].height) - 1:
            nodes[y][x].neighbours.append(nodes[y + 1][x])
            

def shortest_path(x, y):
    for node in all_nodes:
        node.distance = 100000
        node.hops = 0

    start = nodes[y][x]
    start.distance = 0
    all_nodes.sort(key=lambda x: x.distance)

    index = 0
    while len(all_nodes) > index:
        u = all_nodes[index]
        index += 1
        
        for n in u.neighbours:
            tot_dist = u.distance + char_to_int(n.height)
            if tot_dist < n.distance:
                n.distance = tot_dist
                n.hops = u.hops + 1
                if n.height == "E":
                    return n.hops
        
        all_nodes.sort(key=lambda x: x.distance)

# Part 1
# print(shortest_path(20, 0))

# Part 2
paths = []
for y in range(len(data)):
    for x in range(len(data[0])):
        print(x, y, nodes[y][x].height)
        if nodes[y][x].height == "a":
            shortest = shortest_path(x, y)
            if shortest != None:
                paths.append(shortest)

print(min(paths))
