def is_odd(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return False
    return True


a = [1, 3, 5, 7, 9]
print(is_odd(a))