"""
Syntax:
--------
if condition:
    //logic code
    //
    //Indentation
else:
    //Logic code
"""

a = 15
b = 12

if a>b:
    print(a,"is maximum")
else:
    print(b,"is maximum")

"""
odd , even if..else
"""
"""
Syntax:

if condition:
    //logic code
elif condition:
    //logic code
else:
    //logic code
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 :
    if num1 > num3:
        print(num1,"is maximum")
    else:
        print(num3,"is maximum")
elif num2 > num3:
    print(num2,"is maximum")
elif num1 == num2 == num3:
    print("All are equal")
else:
    print(num3,"is maximum")


