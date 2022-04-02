from tkinter import Y


x = 0
y = 8
x = y
y += 1

def copy(a):
    result = [0 for i in range(len(a))]
    for i in range(len(a)):
        result[i] = a[i]
    return result

a = [0,1,2,3,4]
b = copy(a)
c = a
a[1] = 3
print(b)
print(c)