def diag_sum(A):
    d1 = 0
    d2 = 0
    for i in range(len(A)):
        d1 = d1 + A[i][i]
        d2 = d2 + A[i][-i - 1]
    return d1 + d2

n = 3

A = [
    [1, 2, 3],
    [0, -1, 1],
    [2, 2, 1]
]

print(diag_sum(A))