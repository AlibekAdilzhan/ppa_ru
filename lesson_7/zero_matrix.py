n = 3
m = 4

b = []
for i in range(n):
    x = []
    for j in range(m):
        x.append(0)
    b.append(x)

for i in range(n):
    print(b[i])