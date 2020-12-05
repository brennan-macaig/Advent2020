content = []
with open("input/day5.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def get_id(data):
    return int("".join(["1" if i in ["R","B"] else "0" for i in data]), 2)

c = 0
ids = []
for line in content:
    d = get_id(line)
    ids.append(d)
    if c < d:
        c = d
print("highest: " + str(c))

### part 2

res = [ele for ele in range(max(ids)+1) if ele not in ids]

print("missing seat: " + str(res[len(res)-1]))
