# -*- coding: cp1252 -*-

print("Calculator")
v1 = input("Give the first number: ")
v2 = input("Give the second number: ")
v1 = int(v1)
v2 = int(v2)

print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")

s = input("Please select something (1-4): ")
s = int(s)
r1 = "Selection was not correct."

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
else:
    r1 = "Selection was not correct."
    print(r1)
