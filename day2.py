content = []
with open("input/day2.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

## part 1:
# content[i].split = ['n-k', 'c:', 'password']
total = 0
for line in content:
    count = 0
    l = line.split()
    r = l[0].split('-') # r[0] is low, r[1] is high
    c = l[1][0]
    p = l[2]
    for x in p:
        if x == c:
            count += 1
    if count <= int(r[1]) and count >= int(r[0]):
        total += 1
print("total: " + str(total))

## part 2:
total = 0
for line in content:
    count = 0
    l = line.split()
    r = l[0].split('-') # r[0] is low, r[1] is high
    c = l[1][0]
    p = l[2]
    if ((p[int(r[0])-1] == c) != (p[int(r[1])-1] == c)): # xor
        total += 1
print("part2 total: " + str(total))