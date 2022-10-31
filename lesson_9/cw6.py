# A = [
#     [1, 2, 3],
#     [0, -1, 1],
#     [2, 2, 1]
# ]

# B = [
#     [0, -1, 1],
#     [1, 1, 9],
#     [0, 0, 5]
# ]
n = 3
A = [[int(x) for x in input().split()] for i in range(n)]
B = [[int(x) for x in input().split()] for i in range(n)]

C = []

for i in range(len(A)):
    row = []
    for j in range(len(A[i])):
        c = A[i][j] + B[i][j]
        row.append(c)
    C.append(row)

for r in C:
    print(r)