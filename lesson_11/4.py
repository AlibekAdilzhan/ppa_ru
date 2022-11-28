with open("2.txt", "r", encoding="utf-8") as fo:
    lines = fo.readlines()

lines = set(lines)
print(len(lines))

