n = int(input())

a = [["."] * n for i in range(n)]

mid = n // 2
for i in range(n):
    a[i][i] = "*"
    a[i][-i - 1] = "*"
    a[mid][i] = "*"
    a[i][mid] = "*"
for i in range(n):
    s = " ".join(a[i])
    print(s)