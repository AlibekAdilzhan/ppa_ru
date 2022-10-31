def my_sum(a):
    s = 0
    for i in range(len(a)):
        s = s + a[i]
    print(s)


a1 = [1, 2, 3, 4]
a2 = [-1, 1, 1, 0, 1, -1]
a3 = [0, 9, 8, 7, 0, -1]

my_sum(a1)
my_sum(a2)
my_sum(a3)

# s = 0
# for i in range(len(a1)):
#     s = s + a1[i]
# print(s)

# s1 = 0
# for i in range(len(a2)):
#     s1 = s1 + a2[i]
# print(s1)

# s2 = 0
# for i in range(len(a3)):
#     s2 = s2 + a3[i]
# print(s2)