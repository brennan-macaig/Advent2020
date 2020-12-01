content = []
with open("input/day1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
count = 0
for line in content:
    count += 1
    m = int(line)
    for nx in content[count:]:
        n = int(nx)
        if m + n == 2020:
            print("out: " + str((m*n)))
            exit(0)