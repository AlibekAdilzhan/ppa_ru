def my_sum(a):
    s = 0
    for i in range(len(a)):
        s = s + a[i]
    return s


a1 = [1, 2, 3, 4]
a2 = [-1, 1, 1, 0, 1, -1]
a3 = [0, 9, 8, 7, 0, -1]

r1 = my_sum(a1)
r2 = my_sum(a2)
r3 = my_sum(a3)
print(r1, r2, r3)
