"""
loops:
---------------
1) for loop
2) while loop

Syntax:
----------
initialization

while condition:
    //logic code
    increment/decrement (i += 1 , i -= 1)

# i += 1 ---> i = i + 1
# i -= 1 ---> i = i - 1
# """
# i = 1

# while i <= 5:
#     print("Hello",end=" ")
#     i += 1

"""
Task:
-----------
1) 1 to n numbers(user value)
2) n to 1 numbers(user value)
"""

"""
Nested While Loop:
-------------------
1) while loop inside while loop

Syntax:
----------
initalization

while condition:
    intialization
    while condition:
        code
        increment/decrement (i += 1 , i -= 1) 
    incremet/decrement
"""
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

i = 1

while i <= 5:
    j = 1
    while j <= 5:
        print("*",end=" ")
        j += 1
    print()
    i += 1

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3 
4 4 4 4 4
5 5 5 5 5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""