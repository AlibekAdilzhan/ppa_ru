def sq_prod(a):
    s = 1
    for i in range(len(a)):
        s = s * a[i]**2
    return s

# 1 * 4 * 9 * 16 * 25 = 14400
a1 = [1, 2, 3, 4, 5]
print(sq_prod(a1))
