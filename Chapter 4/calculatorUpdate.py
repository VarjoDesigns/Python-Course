# -*- coding: cp1252 -*-

print("Calculator")
v1 = input("Give the first number: ")
v2 = input("Give the second number: ")
v1 = int(v1)
v2 = int(v2)

s = 0
while s != 6:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Change numbers")
    print("(6) quit")
    print("Current numbers: " + str(v1) + str(v2))
    s = input("Please select something (1-6): ")
    s = int(s)

    if s == 1:
        r1 = v1+v2
        r1 = str(r1)
        print("The result is: "+r1)
    elif s ==  2:
        r1 = v1-v2
        r1 = str(r1)
        print("The result is: "+r1)
    elif s ==  3:
        r1 = v1*v2
        r1 = str(r1)
        print("The result is: "+r1)
    elif s ==  4:
        r1 = v1/v2
        r1 = str(r1)
        print("The result is: "+r1)
    elif s ==  5:
        v1 = input("Give the first number: ")
        v2 = input("Give the second number: ")
        v1 = int(v1)
        v2 = int(v2)
    elif s ==  6:
        print("Thank you!")
    else:
        r1 = "Selection was not correct."
        s = 0
        print(r1)
