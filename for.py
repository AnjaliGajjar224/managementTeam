"""
for(initialization;condition;increment/decrement)

Syntax:
-------------
for i in range(start,end,step):
    code
"""
# for i in range(5):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# for i in range(1,15,3):
#     print(i)

# for i in range(15,0,-2):
#     print(i)

# myStr = "Hello World"

# for i in myStr:
#     print(i)

# n = int(input("Enter element:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# if num1 > num2:
#     print(num1,"is maximum")
# else:
#     print(num2,"is maximum")


print(num1,"is maximum") if num1 > num2 else print(num2,"is maximum")