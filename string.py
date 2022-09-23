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
# """

# myStr = input("Enter your String: ")

# print(myStr)

# print("Length of the String is: ",len(myStr))

# index = int(input("Enter your index: "))

# print("Character at index",index,"is:",myStr[index])
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


# a = 10
# b = 5

# print(a,"+",b,"=",a+b)

# print(f"{a} + {b} = {a+b}")

s = "Python iS a ProgramMing LAnguage"

# print("Royal Technosoft Pvt. Ltd. Since {} to {}".format(2015,2022))

# print("Royal Technosoft Pvt. Ltd. Since {y1} to {y2}".format(y2 = 2050 , y1 = 2010))

# print(s.find("a"))        # return index of first occurence
# print(s.rfind("a"))       # right to left <---

# print(s.find("a",11))     # start = 11 to length

# print(s.index("a"))       # return index of first occurence
# print(s.rindex("a"))

# print(s.index("a",11))

# print(s.find("b"))        # return -1 if not found
# print(s.index("b"))       # return error if not found

# print("ABCD123".isalnum())      # if string contains alphabets or numeric values then it returns true
# print("ABC".isalnum())
# print("1234".isalnum())
# print("123@$ABC".isalnum())

# print("ABCD".isalpha())
# print("1234ABCD".isalpha())

# s5 = "2022"
# print(s5.isdecimal())   # considers strictly plain digits from 0 to 9 only, nothing else
# print(s5.isdigit())     # considers subscripts, superscripts and circled numbers also as numbers
# print(s5.isnumeric())   # considers vulgar fractions, roman numerals, numbers from other languages

# s6 = "2⁸"
# print(s6)
# print(s6.isdecimal())
# print(s6.isdigit())
# print(s6.isnumeric())

# s7 = "②⓪②②"
# print(s7)
# print(s7.isdecimal())
# print(s7.isdigit())
# print(s7.isnumeric())


# s8 = "¼"
# print(s8)
# print(s8.isdecimal())
# print(s8.isdigit())
# print(s8.isnumeric())


# s9 = "二千二十二"
# print(s9)
# print(s9.isdecimal())
# print(s9.isdigit())
# print(s9.isnumeric())


# s10 = "IV"
# s11 = "Ⅵ"
# print(s10)
# print(s10.isnumeric())
# print(s11)
# print(s11.isnumeric())

# print("ABCD123".isascii())

# print("num1".isidentifier())
# print("1Num".isidentifier())
# print("num 1".isidentifier())

# print("abcd".islower())

# print("ABCD".isupper())

# print("Python Is A Fun.".istitle())

# print("Are you #1?".isprintable())
# print("Are you \n#1?".isprintable())

# print("       Hello      ".isspace())
# print("     ".isspace())
# print("\t".isspace())
# print("\n".isspace())

# s1 = "Hello"
# s2 = "Bye" 
# l = ["Royal","Hey","Why"]

# print(s1.join(s2))
# print(s1.join(l))


# print(s.lower())
# print(s.upper())
# print(s.title())

# print("Hello".ljust(10))
# print("Hello".ljust(10,"*"))

# print("Hello".rjust(10))
# print("Hello".rjust(10,"-"))

# print("       Hello".lstrip())
# print("$$$$$$$$Hello".lstrip("$"))

# print("    Hello      ".rstrip())
# print("    Hello$$$$".rstrip("$"))

# print("        Hello      ".strip())
# print("$$$$$$$$HELLO$$$$$$$$$$$".strip("$"))\

# s = "Royal_Technosoft_Pvt_Ltd"

# print(s.partition("_"))

# print(s.rpartition("_"))

# print(s.replace("_"," "))

# print(s.split("_",2))

# print(s.rsplit("_",2))

# print(s.swapcase())

# s1 = "Hello\nHye\nBye"

# print(s1.splitlines())

# text = "Hello"

# print(text.zfill(10))               # 10 - 5 = 5 

# date = "1-10-2022"

# print(date.zfill(10))

"""
1. Take a Full name from the user and print abbre. of them.

e.g. 

Input: Anjali Rakesh Gajjar

Output: A.R.Gajjar
"""
