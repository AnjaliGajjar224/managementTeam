"""
Loops:
--------------
1. Entry Controlled Loops  e.g. while, for
2. Exit Controlled Loops   e.g. do..while


while loops:
--------------

Syntax:

initialization

while condition:
    statements
    increment/decrement
# # """
# i = 1         # initialization

# while i <= 5:    # condition
#     print("Hello",end="--")
#     i += 1       # increment/decrement

# i = 1
# n = int(input("Enter a number: "))

# while i <= n:
#     print(i,end="_")
#     i += 1


# i = int(input("Enter a number : "))

# while i > 0:
#     print(i,end="--")
#     i -= 1

"""
Take a number from the user and print sum of all the numbers
e.g. n = 5
     1+2+3+4+5 = 15
"""
# n = int(input("Enter a number : "))
# sum = 0
# i = int(input("Enter starting range:"))

# while i <= n :
#     if i < n:
#         print(i,end="+")
#         sum += i
#     else:
#         print(i,end="=")
#         sum += i
#     i += 1

# print(sum)
"""
Take a number and print the table of that number upto 10
# """
# n = int(input("Enter a number : "))

# i = 1

# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i += 1

"""
Take number from the user and print sum of all the even numbers and print odd numbers.
e.g.
n = 10
sum of even numbers = 2+4+6+8+10 = 30
Odd numbers: 1 3 5 7 9 
"""

# n = int(input("Enter a number : "))

# i = 1
# sum = 0
# while i <= n:
#     if i%2 == 0:
#         print(i,end="+")
#         sum += i
#     i += 1

# print("=",sum)

# i = 1
# print("Odd numbers: ")
# while i <= n:
#     if i%2 == 1:
#         print(i,end=" ")
#     i += 1

"""
Take n from the user and multiply all the numbers 

e.g. n = 5
        1*2*3*4*5 = 120
"""

# n = int(input("Enter a number : "))

# i = 1
# mul = 1
# while i <= n:
#     if i < n:
#         print(i,end=" x ")
#         mul *= i
#     else:
#         print(i,end="=")
#         mul *= i
#     i += 1

# print(mul)

"""
Nested While loop:
-------------------

Syntax:

initialization

while condition:
    statements
    intialization
    while condition:
        statements
        increment/decrement
    increment/decrement
"""

# i = 1

# while i <= 5:
#     j = 1
#     while j <= 10:
#         print(i,"x",j,"=",i*j)
#         j += 1
#     print()
#     i += 1

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# i = 1

# while i <= 5:
#     j = 1
#     while j <= 5:
#         print("*",end=" ")
#         j += 1
#     print()
#     i += 1

"""
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
# i = 1

# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(i,end=" ")
#         j += 1
#     print()
#     i += 1

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(j,end=" ")
#         j += 1
#     print()
#     i += 1

"""
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""
# i = 1
# num = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(num,end=" ")
#         num += 1
#         j += 1
#     print()
#     i += 1

"""
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
"""

# i = 1

# while i <= 5:
#     j = 1
#     while j <= 5:
#         if j % 2 == 0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         j += 1
#     print()
#     i += 1

"""
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
"""
# i = 1

# while i <= 5:
#     j = 1
#     while j <= 5:
#         if i % 2 == 0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         j += 1
#     print()
#     i += 1
"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
"""
# i = 0
# ch = 65
# while i < 5:
#     j = 1
#     while j <= 5:
#         print(chr(ch+i),end=" ")
#         j += 1
#     print()
#     i += 1

"""
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
"""

# i = 1
# ch = 65
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(chr(ch),end=" ")
#         ch += 1
#         j += 1
#     print()
#     i += 1

"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""

"""
*
* *
* * *
* * * *
* * * * *
"""

"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

# i = 5

# while i >= 1:
#     j = 5

#     while j >= i:
#         print(j,end = " ")
#         j -= 1

#     print()
#     i -= 1

"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""
i = 1

while i <= 5:
    j = i

    while j <= 5:
        print(j,end = " ")
        j += 1
    print()
    i += 1        

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""