a = "abcdefgchicjkc"
b = ""
change_index = 2
c = 0
for i in range(len(a)):
    if c == change_index and a[i] == "c":
        b = b + "Z"
    else:
        b = b + a[i]
    if a[i] == "c":
        c = c + 1
print(b)