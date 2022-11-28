with open("1.txt", "r", encoding="utf-8") as fo:
    lines = fo.readlines()

lines = [line.split("\t") for line in lines]
lines = [[line[1], line[2].strip()] for line in lines]
set_1 = []
set_2 = []
for l in lines:
    set_1.append(l[0])
    set_2.append(l[1])


set_1 = set(set_1)
set_2 = set(set_2)
set_main = set_1.union(set_2)
set_main = list(set_main)
for s in set_main:
    print(s)

print()
print(len(set(set_1)))
print(len(set(set_2)))