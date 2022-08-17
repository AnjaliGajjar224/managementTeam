

# print("Hello World")
# print('Hello World')

# Single Line Comment
"""
Multi
Line
Comments
"""

'''
Multi
Line
Comments
'''

"""
Escaping Characters/Sequences

\n ---> new line
\t ---> tab
\b ---> backspace
\r ---> carriage return
\
"""
# print("How are\b you?")
# print("Python is a fun \rJAVA")
"""
Numeric Data types:

1. Integer
2. Float
3. Complex Numbers

Python is an implicit bind language
"""

# num1 = 15
# num2 = 12.13
# num3 = 2+5j

# print(type(num1))

# print("Number 1 is: ",num1)

"""
Arithmetic Operators
+, - , * ,/ , // , ** , %
"""
# print(15/2)
# print(15//2)
# print(15%2)
# print(15**2)         # 15 * 15 = 225

# print(pow(5,5))

"""
Comparison Operators

< , > , <= , >= , == ,!=

Bitwise Operators

& , | , ^ , >> ,<< 

Logical Operators

and(&&) , or(||) , not(~)

Membership Operators
in , not in 
"""

# print('b' in 'banana')
# print('k' in 'banana')

# print('b' not in 'banana')
# print('k' not in 'banana')

"""
Conditional Statements

if , elif ,else 

Syntax:

if condition:
    statements
elif condition:
    statements
...
else:
    statements
"""

"""
Loops:
---------
1. while
2. for

Syntax:

intialization

while condition:
    do something
    increment/decrement

Syntax:

for var_name in range(start,end,step):
    do something

for var_name in collection_name:
    do something
"""

"""
Armstrong Numbers:

e.g. 153

digits = 3

153 = 1^3 + 5^3 + 3^3
    = 1 + 125 + 27
    = 153

num == sum

Armstrong Numbers

153 , 370 , 371 , 407

Take starting range and ending range from the user and find all the armstrong numbers between them

e.g. start = 100 end = 200

output: 
153
"""

# start = int(input("Enter Starting range: "))
# end = int(input("Enter Ending range: "))

# for num in range(start,end+1):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** len(str(num))
#         temp //= 10
#     if num == sum:
#         print(num,end=" ")

"""
Take a  starting range and ending range from the user and find all the palindrome numbers between them.

e.g. 121 , 1221 , 12321...
"""

# start = int(input("Enter Starting range: "))
# end = int(input("Enter Ending range: "))

# for num in range(start,end+1):
#     rev = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp //= 10
#     if num == rev:
#         print(num,end=" ")

"""
H.W.
------------------------------
Take a  starting range and ending range from the user and find all the prime numbers between them.
"""

"""
5 4 3 2 1
4 3 2 1 
3 2 1
2 1 
1

5 
5 4 
5 4 3
5 4 3 2
5 4 3 2 1

      *
     ***
    *****
   *******

   *
  ***
 *****
 *****
  ***
   *

"""

"""
while..else
for...else
# """
# i = 1

# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print("else")

# for i in range(1,10):
#     print(i)
# else:
#     print("else")
"""
Control Statements:
------------------
1. break
    break the loop

2. continue
    continue the loop without executing the statements

3. pass
    pass the control to the next statement
"""

# for i in range(1,11):
#     if i == 5 :
#         break
#     print(i)

# for i in range(1,11):
#     if i == 5 :
#         continue
#     print(i)

# for i in range(1,11):
#     pass


# for i in range(1,11):
#     if i == 5 :
#         break
#     print(i)
# else:
#     print("else")



















