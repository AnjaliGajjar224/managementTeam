from tkinter import N


print("Hello World")
print('Hello World')

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
print("How are\b you?")
print("Python is a fun \rJAVA")
"""
Numeric Data types:

1. Integer
2. Float
3. Complex Numbers

Python is an implicit bind language
"""

num1 = 15
num2 = 12.13
num3 = 2+5j

print(type(num1))

print("Number 1 is: ",num1)

"""
Arithmetic Operators
+, - , * ,/ , // , ** , %
"""
print(15/2)
print(15//2)
print(15%2)
print(15**2)         # 15 * 15 = 225

print(pow(5,5))

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

print('b' in 'banana')
print('k' in 'banana')

print('b' not in 'banana')
print('k' not in 'banana')

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

n = int(input("Enter number: " ))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit**3                   # sum = sum + digit ** 3 
    temp //= 10                       # temp = temp // 10

if n == sum:
    print(n,"is Armstrong")
else:
    print(n,"is not Armstrong")
