b = [
    [1, 2, 3, 4],
    [1, 0, -1, 5],
    [3, 99, 1, 7]
]

s = 0

for i in range(len(b)):
    for j in range(len(b[i])):
        s = s + b[i][j]

print(s)