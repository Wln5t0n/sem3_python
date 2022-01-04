tup1 = ( 1, 2, 3, 4, 5, 6, 7, 8, 9)
tup4 = ( 10, 11, 12, 13 )
tup2 = ( "MAKEUSEOF" )

list1 = [1, 2, 3, 4, 5, 6]
tup3 = tuple(list1)

total = tup1 + tup4
#print("counts number of times 4 occurs in the tuple")
print( tup1.count(4) )

#print("Finding the Position of an Element in a Tuple")
print( tup1.index(4) )

#How to Convert String to a Tuple
print( tup2 )

#print("List to a Tuple")
print(tup3)

#How to Join Two or More Tuples
print( total )

#How to Multiply Tuples
total = tup4 * 2
print( total )

#How to Find Total Number of Elements in a Tuple
print( len( tup1 ) )

#How to Find Minimum Element in a Tuple
print("Minimum element in the tuple is: ", min(tup1))

#How to Find Maximum Element in a Tuple
print("Maximum element in the tuple is: ", max(tup1))

#How to Find the Sum of All Elements in a Tuple
print("Sum element in the tuple is: ", sum(tup1))

#any() Operation on Tuples
tup1 = ( False, False, False, True )
print( any( tup1 ) )

#all() Operation on Tuples
print( all( tup1 ) )

#sorted() Operation on Tuples
tup1 = ( 6, 1, 8, 3, 7, 2 )
print( sorted(tup1) )
print( type(sorted( tup1 )) )
# Note that the return type is list

#How to Shuffle a Tuple

import random
old_tuple = ( 45, 46, 47, 48, 49 )

# Printing tuple
print("Old tuple:", old_tuple)


# Typecasting tuple to list
list1 = list(old_tuple)

# Shuffling list
random.shuffle(list1)

# Typecasting list back to tuple
new_tuple = tuple(list1)

# Printing new shuffled tuple
print("New shuffled tuple:", new_tuple)


#How to Convert List of Tuples to List of Lists

list1 = [ ('A', 'B'), ('C', 'D'), ('E', 'F') ]
print("List of tuples:", list1)

# List Comprehension
result = [ list(element) for element in list1 ]
print("List of lists:", result)

#How to Reverse a Tuple
old_tuple = ('M', 'A', 'K', 'E', 'U', 'S', 'E', 'O', 'F')
print("Old tuple:", old_tuple)

# Reversing tuple using slicing
new_tuple = old_tuple[::-1]
print("New tuple:", new_tuple)


#output
"""
3
MAKEUSEOF
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
(10, 11, 12, 13, 10, 11, 12, 13)
9
Minimum element in the tuple is:  1
Maximum element in the tuple is:  9
Sum element in the tuple is:  45
True
False
[1, 2, 3, 6, 7, 8]
<class 'list'>
Old tuple: (45, 46, 47, 48, 49)
New shuffled tuple: (48, 49, 46, 47, 45)
List of tuples: [('A', 'B'), ('C', 'D'), ('E', 'F')]
List of lists: [['A', 'B'], ['C', 'D'], ['E', 'F']]
Old tuple: ('M', 'A', 'K', 'E', 'U', 'S', 'E', 'O', 'F')
New tuple: ('F', 'O', 'E', 'S', 'U', 'E', 'K', 'A', 'M')
"""