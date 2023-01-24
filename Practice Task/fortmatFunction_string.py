fname="Anik"
lname='Sen'

FullName="{} {}".format(fname,lname)
print("Hello i'm ",FullName,end="")
'''Each variable is referred to by a set of braces; the braces will be filled
by the values listed in parentheses in the order provided:'''

district="Moulvibazar"
upozila=' Sreemangol'

print(" from {0},{1}".format(district,upozila))
'''use of {0} to indicate the first argument to the
format method. Similarly, the second specification is {1}
corresponding to the second argument to the format method.'''

id=42138
dept='CSE'
print('I am from {dept} & my id is {id}'.format(dept=dept,id=id))