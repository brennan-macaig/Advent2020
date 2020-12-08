import string
content = []
with open("input/day6.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

arr = []
tmp = ""
for line in content:
    if line == "":
        arr.append(tmp)
        tmp = ""
        continue
    tmp = tmp + line
    
arr.append(tmp)
count = 0
for elem in arr:
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for x in elem:
        d[x] = 1
    for _, val in d.items():
        if val > 0:
            count += 1

print(count)


## part 2
arr = {} # {groupID: ["list", "of", "group", "inputs"]}
c = 0
tmp = ""
count = 0
for line in content:
    if line == "":
        c += 1
        continue

    if c not in arr:
        arr[c] = [line]
    else:
        arr[c].append(line)

for _, val in arr.items():
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for x in val:
        # iterate over list items
        for elem in x:
            d[elem] += 1
    # check
    for _, v in d.items():
        if v == len(val):
            count += 1
print("part 2: ", str(count))

