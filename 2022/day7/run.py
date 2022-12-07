f = open('input.txt', 'r')
data = f.readlines()

class dir:
    def __init__(self, name, sub_dirs, files):
        self.name = name
        self.sub_dirs = sub_dirs
        self.files = files

    def show(self, layer):
        print("-"*layer + self.name.split('\n')[0] + " (dir)")
        for i in self.sub_dirs:
            i.show(layer+1)
        for i in self.files:
            print("-"*(layer+1) + i.name.split('\n')[0] + " (file)")
    
class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def ls(directory):
    directory.name = data.pop(0).split(" ")[2] #$ cd a
    data.pop(0) # ls
    item = data[0]
    while len(data) > 0 and item[0] != '$':  
        size_or_dir, name = item.split(" ")
        if size_or_dir.isnumeric():
            directory.files.append(file(name, int(size_or_dir)))
        else:
            directory.sub_dirs.append(dir(name, [], []))

        data.pop(0)
        if len(data) != 0:
            item = data[0]

    for sub_dir in directory.sub_dirs:
        ls(sub_dir)
        if len(data) != 0:
            if data[0] == "$ cd ..\n":
                data.pop(0)

    return directory

root = ls(dir("root", [], []))

#root.show(0)

sizes = []

def get_size(directory):
    dir_size = 0

    for sub_dir in directory.sub_dirs:
        dir_size += get_size(sub_dir)

    for file in directory.files:
        dir_size += file.size

    # Part 1
    # if dir_size < 100000:
    #     sizes.append(dir_size)

    # Part 2
    sizes.append(dir_size)

    return dir_size

get_size(root)

# Part 1
# sum = 0
# for s in sizes:
#     sum += s
# print(sum)

# Part 2
sizes.sort()
s = 70000000 - sizes[-1]
res = 0
for i in sizes:
    if i + s >= 30000000:
        res = i
        break

print(res)