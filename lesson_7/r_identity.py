n = int(input())

a = [[0] * n for i in range(n)]

for i in range(n):
    a[i][-i - 1] = 1

for i in range(n):
    print(a[i])