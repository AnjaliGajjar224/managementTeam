"""
String --> it is array of characters
"""

# s = 'Royal'

# print(s)
# print(type(s))

# ch = 'a'

# print(ch)
# print(type(ch))

"""
Indexing
        Positive Indexing       Negative Indexing
R       0                           -5
o       1                           -4
y       2                           -3
a       3                           -2
l       4                           -1
"""

# print("First Character is: ",s[0])       # R
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# # print(s[5])

# # Negative Indexing

# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# print(s[-6])

# Length of the String

# print("Length of the String is: ",len(s))
# print(s)

"""
Take a string from the user and find length of the string . Take index from the user and print character on that specific index. 
"""

"""
Slicing of the String:-
---------------------------
1. [start:end]
2. [start:]
3. [:end]
4. [:]
5. [start:end:step0]
"""
s = "Royal_Technosoft_Pvt_Ltd."        


# print("Length of the String is: ",len(s))

# print("Original String is:\n\n",s)

# Slicing

# print("Substring is: ")

# print(s[0:20])                 # 0 to 19(20 is not include)
# print(s[20])

# print(s[1:20])

# print(s[5:24])

# print(s[-25:-15])


# # 2. [start: ]


# print(s[12:])       # start = 12 to len(s)
# print(s[-18:])      # start= -18 to -1


# # 3. [:end]

# print(s[:20])      # start = 0 to 19 (20 is not included)
# print(s[:-5])      # start = -25 to -6 (-5 is not included)

# # 4.[:]

# print(s[:])

# print(s[-1:-20])
# print(s[20:10])

# Reverse String

# print(s[-1:-20:-1])
# print(s[20:10:-1])

# 5. [start:end:step]

# print(s[2:20:1])
# print(s[2:20:2])

# print(s[-20:-10:2])

# print(s[-1:-20:-2])

"""
Take a string from the user and take starting, ending and stepping from the user and find substring of it.
"""

s = "Python is a ProGramming LanGuagE."
# print(len(s))
"""
String is immutable and ordered.

Immutable means It doesn't change the original string by its methods.
"""

# print(s.capitalize())

# print(s.count("G"))
# print(s.count("G",1,16))                 # count("string",starting index,ending index)

# print(s.casefold())

# print(s.center(30))
# print(s.center(51))                   # 51 - len(s) = 51 - 33 = 18 --> 18/2 --> 9 both side

# print(s.center(51,"*"))

# print(s.center(36,"$"))

# s1 = s.center(71,"|")
# print(s1)

# print(s.encode())                  # by default UTF - 8

# if s == s.encode():
#     print("TRUE")
# else:
#     print("FALSE")

# print(s.endswith("."))
# print(s.endswith("Language"))
# print(s.endswith("LanGuagE."))

# print(s.startswith("Python"))

# s1 = "Hello\tHye\tBye"

# print(s1)
# print(s1.expandtabs(20))
