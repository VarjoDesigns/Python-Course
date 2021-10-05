# -*- coding: cp1252 -*-

n = input("Give a number: ")
n = int(n)

x = 0
i = 0

while i < n:
    x += i
    i += 1

x = str(x)
print("The sum was: " + x)
