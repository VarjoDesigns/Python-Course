# -*- coding: cp1252 -*-

n1 = input("Give a number: ")
n1 = int(n1)

n2 = input("Give another number: ")
n2 = int(n2)

if (n1 % 2 == 0) and (n2 % 2 == 0):
    print("Both numbers are even.")
elif (n1 % 2 == 0) or (n2 % 2 == 0):
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")
