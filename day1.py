def part1(content):
    count = 0
    for mx in content:
        count += 1
        m = int(mx)
        for nx in content[count:]:
            n = int(nx)
            if m + n == 2020:
                print("out: " + str(m) + " * " + str(n) + " = " + str((m*n)))

def part2(content):
    count = 0
    for mx in content:
        count += 1
        m = int(mx)
        count2 = 1
        for nx in content[count:]:
            count2 += 1
            n = int(nx)
            for kx in content[count2:]:
                k = int(kx)
                if (m + n + k) == 2020:
                    print("out: " + str(m) + " * " + str(n) + " * " + str(k) + " = " + str(m*n*k))

content = []
with open("input/day1.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
part1(content)
part2(content)