"""
54321
4321
321
21
1
"""


# i = 5

# while i >= 1:
#     j = i

#     while j >= 1:
#         print(j,end=" ")
#         j -= 1

#     print()
#     i -= 1

"""
for..else
# """
# for i in range(5):
#     print(i)
# else:
#     print("Loop is over")

"""
Assignment Operators:

=     Assignment
+=    Add and assign (i += 1 ----> i = i + 1)
-=    Subtract and assign (i -= 1 ----> i = i - 1)
*=    Multiply and assign (i *= 1 ----> i = i * 1)
/=    Divide and assign (i /= 1 ----> i = i / 1)
%=    Modulus and assign (i %= 1 ----> i = i % 1)
//=   Floor division and assign (i //= 1 ----> i = i // 1)
**=   Exponent and assign (i **= 1 ----> i = i ** 1)
"""

# a = 5
# print(a)

# a += 5
# print(a)

# a -= 4
# print(a)

"""
BIitwise Operators:

&    Bitwise AND
|    Bitwise OR
^    Bitwise XOR
<<   Shift left
>>   Shift right

45 - 101101
43 - 101011

2| 43
2 | 21 ---> 1
2 | 10 ---> 1
2 | 5 ----> 0
2 | 2 ---> 1
2 | 1 ---> 0

1) & Bitwise AND

a   b   a&b
0   0   0
0   1   0
1   0   0
1   1   1

45 - 1 0 1 1 0 1 
&    & & & & & &
43 - 1 0 1 0 1 1 
------------------
     1 0 1 0 0 1 
"""
# print(45&43)
"""
2) | Bitwise OR

a   b   a&b
0   0   0
0   1   1
1   0   1
1   1   1

45 - 1 0 1 1 0 1 
|    
43 - 1 0 1 0 1 1 
------------------
     1 0 1 1 1 1  

"""
# print(45|43)
"""
3) ^ Bitwise XOR

a   b   a^b
0   0   0
0   1   1
1   0   1
1   1   0

45 - 1 0 1 1 0 1 
^    
43 - 1 0 1 0 1 1 
------------------
     0 0 0 1 1 0 

"""
# print(45^43)
"""
4) >> Shift right

45 - 1  0  1  1  0    1 
     32  16  8  4  2  1   
45>>1    1   0  1  1  0   
45>>2        1   0  1  1  
"""
# print(45>>2)
"""
5) << Shift left

3 - 11

3 << 5 


3 - 11                                              1     1
    512    256    128    64    32    16    8    4    2    1

 3<< 2                                     1     1    0   0
 3 <<4                          1     1    0   0      0   0
 3 << 5                  1       1    0    0     0   0   0
"""
# print(3<<5)

"""
Logical Operators

1) and
2) or
3) not
"""
# print(15> 10 and 15>20)

# print(15> 10 or 15>20)

# print(not(15> 10))

