course=['oop','DS','algo','OS']
print(course)
'''square brackets ([]) indicate a list, and individual elements
in the list are separated by commas.'''
print(course[2]) #3rd index
print(course[-1]) #last index

course[0]='PL'
print(course)

course.append('COA')
print(course)
'''• The simplest way to add a new element to a list is to append the item
to the list by using the append() method.'''

course.insert(2,'Micro')
print(course)
'''add a new element at any position in a list by using the insert() method.'''

del course[0]
print(course)
'''If you know the position of the item you want to remove from a list,
you can use the del statement.'''

popel=course.pop()

print(popel," is poped")
print(course)

popel=course.pop(0)

print(popel," is poped")
print(course)

'''How to decide between del and pop(): when you want to delete an item from a list and
not use that item in any way, use the del statement; if you want to use an item as you
remove it, use the pop() method.'''






