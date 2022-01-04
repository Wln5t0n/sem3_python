myList = [1, 2, 3, 'Test', 'Tilak Maharashtra Vidyapeeth Pune'] 

#append()

myList.append(4)
myList.append(5)
myList.append(6)

for i in range(7, 9):
	myList.append(i)

print(myList)

"""
output:- [1, 2, 3, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8]
"""

#extend()

myList.extend([9, 10, 11])

for i in range(12, 14):
	myList.append(i)

print(myList)

"""
output:- [1, 2, 3, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""

#insert()

myList.insert(3, 4)
myList.insert(4, 5)
myList.insert(5, 6)

print(myList)

"""
output:- [1, 2, 3, 4, 5, 6, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""

#index()

print(myList.index('Test'))            # searches in the whole list
print(myList.index('Test', 6, 7))     # searches from 0th to 2nd position

"""
Output:-
[1, 2, 3, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8]
[1, 2, 3, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
[1, 2, 3, 4, 5, 6, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
6
6
"""

#sort()

yourList = [4, 2, 6, 5, 0, 1] 
yourList.sort()
print(yourList)

"""
output:-
[1, 2, 3, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8]
[1, 2, 3, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
[1, 2, 3, 4, 5, 6, 'Test', 'Tilak Maharashtra Vidyapeeth Pune', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
6
6
[0, 1, 2, 4, 5, 6]

"""