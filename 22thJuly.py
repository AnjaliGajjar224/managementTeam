"""
Arithmetic Operators
+ , - , * , / , % , // , **
Comarison Operators
== , != , > , < , >= , <=
Bitwise Operators
& , | , ^ , << , >>
Logical Operators
and , or , not
Assignment Operators    
= , += , -= , *= , /= , %= , //= , **=
Membership Operators
in , not in
Identity Operators
is , is not
"""
# Membership Operators

print('b' in 'banana')              # True
print('n' in 'banana')              # True
print('nan' in 'banana')            # True

print('k' in 'banana')              # False

print('b' not in 'banana')          # False
print('k' not in 'banana')          # True

# for i in range(1, 10):
#     print(i, end=' ')

if 'b' in 'banana':
    print('b is in banana')
else:
    print('b is not in banana')

"""
Take string as input from user and take another string as input from user and check if the second string is in a first string or not. 
"""
str = input("Enter a string: ")

char = input("Enter a character: ")

if char in str:
    print("'",char,"'","is in '",str,"'")
else:
    print(char,"is not in",str)

"""
'd' is present in  'Good Morning' String
"""

