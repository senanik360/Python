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

course.remove('algo')
print(course)

'''• If you only know the value of the item you want to remove, you can
use the remove() method.
• The remove() method deletes only the first occurrence of the value
you specify. If there’s a possibility the value appears more than once
in the list, you’ll need to use a loop to make sure all occurrences of
the value are removed.'''
course=['oop','ds','algo','os']
course.sort()
print("Courses list after sort\n",course)

course.sort(reverse=True)
print(course)
'''sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.'''
print(sorted(course))
'''To maintain the original order of a list but present it in a sorted order, you can use the
sorted() function.'''
print(course)

course.reverse()
'''reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list.

The reverse() method changes the order of a list permanently, but you can
revert to the original order anytime by applying reverse() to the same list a
second time.'''
print(course)

print("total number of course",len(course)) 
'''find the length of a list by using the len() function.'''




