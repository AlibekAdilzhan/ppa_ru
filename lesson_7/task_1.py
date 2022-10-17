n, m = [int(x) for x in input().split()]

a = [[int(x) for x in input().split()] for i in range(n)]

index_i = 0
index_j = 0
maxi = a[0][0]

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > maxi:
            maxi = a[i][j]
            index_i = i
            index_j = j


print(index_i, index_j)