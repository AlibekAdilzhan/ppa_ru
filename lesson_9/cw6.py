def sum_matrix(A, B):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            c = A[i][j] - B[i][j]
            row.append(c)
        C.append(row)
    return C


n = 3
A1 = [[int(x) for x in input().split()] for i in range(n)]
B1 = [[int(x) for x in input().split()] for i in range(n)]
C = sum_matrix(B1, A1)

for r in C:
    print(r)