import random

n = 3
a = [[random.randint(1, 1000) for i in range(n)] for j in range(n)]

for i in range(len(a)):
    print(a[i])