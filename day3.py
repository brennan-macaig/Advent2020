content = []
with open("input/day3.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

## part1
# right 3, down 1
idx = 0
c = 0
for line in content:
    idx = idx % len(line)
    if line[idx] == "#":
        c += 1
    idx += 3
print("r3, d1: %d", c)

print("*********** part 2")

idx = 0
c = 0
for line in content:
    idx = idx % len(line)
    if line[idx] == "#":
        c += 1
    idx += 1
print("right 1, down 1: %d", c)
mul = c

idx = 0
c = 0
for line in content:
    idx = idx % len(line)
    if line[idx] == "#":
        c += 1
    idx += 3
print("r3, d1: %d", c)
mul *= c

idx = 0
c = 0
for line in content:
    idx = idx % len(line)
    if line[idx] == "#":
        c += 1
    idx += 5
print("r5 d1: %d", c)
mul *= c

idx = 0
c = 0
for line in content:
    idx = idx % len(line)
    if line[idx] == "#":
        c += 1
    idx += 7
print("r7 d1: %d", c)
mul *= c

idx = 0
c = 0
for line in content[::2]:
    idx = idx % len(line)
    if line[idx] == "#":
        c += 1
    idx += 1
print("r1 d2: %d", c)
mul *= c
print(mul)
