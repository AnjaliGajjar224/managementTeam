"""
List is one of the collection of Python.
List is a mutable & ordered.
It allowes multiple datatypes in single list.
To defined list we are using [](square brackets).
"""

# l = ["Royal",15,25.52,5+2j]

# print("List is: ",l)
# print("Type: ",type(l))

# for i in l:
#     print(type(i))
#     print(i)

# Indexing

# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])


# print(l[-1])
# print(l[-2])
# print(l[-3])
# print(l[-4])

"""
Slicing of the List:
-----------------------------
1. [start:end]
2. [start:]
3. [:end]
4. [:]
5. [start:end:step]
"""

# print(l[0:2])

# l = [1,2,3,4,5]

# print(l[::2])

# myList = [1,2,23,34,45,56,7,18,90,10]

# print("Length : ",len(myList))
# print("Maximum: ",max(myList))
# print("Minimum: ",min(myList))
# print("Sum: ",sum(myList))
# print("Sorted List is: ",sorted(myList))            # Ascending order by default
# print("Sorted List is: ",sorted(myList,reverse=True))          # Descending order

# List1 = ["Bannaa","cherry","apple","Apple","Airplane","ball","Dog"," "]


# print("Length : ",len(List1))
# print("Maximum: ",max(List1))

"""
ASCII VALUES:
------------------

A - 65 
B - 66
C - 67 ...So on 

a - 97
b - 98
c - 99 ...So on 

_(space) - 32
"""
# print("Minimum: ",min(List1))
# # print("Sum: ",sum(List1))                     # It gives TypeError
# print("Sorted List is: ",sorted(List1))            # Ascending order by default
# print("Sorted List is: ",sorted(List1,reverse=True))          # Descending order

# l = [12,32,45,65,78,90,2,6,4,87,5,4,10]

# l.append(5)          # append method will add element at the end of the list
# print(l) 

# l = []        # Null list

# for i in range(5):
#     l.append(int(input("Enter element: ")))

# print(l)

L1 = [12,43,56,78,9,32,7,90,23,67,3,2,12,12,32]

# print(L1.count(12))

# l2 = L1.copy()

# print(l2)

# l3 = L1
# print(l3)


"""
Identity Operators
1. is
2. is not
"""
# print(id(L1))
# print(id(l2))
# print(id(l3))

# print(L1 is l3)        # True
# print(L1 is l2)        # False

# l2.clear()       # it clear all the elements from the list

# print(l2)

# del l2
# print(l2)

# l = [12,34,56,78]
# L1.extend(l)

# print(L1)

# L1.extend([9])
# print(L1)

# print(L1.index(56))

# L1.insert(0,15)
# print(L1)

# L1.pop(0)         # it takes index as a parameter and remove element on that specific index
# print(L1)

# L1.remove(90)      # it takes element as a parameter
# print(L1)

# L1.reverse()
# print(L1)

# l = L1[::-1]
# print(l)

# L1.sort()
# print(L1)

# L1.sort(reverse=True)
# print(L1)

