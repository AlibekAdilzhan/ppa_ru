n = 3
b = [
    [1, 2, 3, 4],
    [1, 0, -1, 5],
    [3, 99, 1, 7]
]

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=" ")
    print()

for i in range(len(b)):
    print(b[i])

print(b)
