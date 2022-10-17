n = 3
m = 4

a = [[0] * n for i in range(m)]

a[1][2] = 99

for i in range(len(a)):
    print(a[i])