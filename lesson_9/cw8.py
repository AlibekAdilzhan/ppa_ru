# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

def fibo_2(n):
    a = [0, 1]
    for i in range(n - 1):
        c = a[-1] + a[-2]
        a.append(c)
        a.pop(0)
    return a[-1]


n = int(input())
print(fibo_2(n))