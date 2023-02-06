member = {'anik':'cse', 'alok':12, 'anushree':1, 'adri':'n/a'}

print(member['anik'])


info={"a":"Cse",'b':'eee','c':'ipe'}

print(info)

for name, dept in info.items():
    print(name.title(), dept.title())
'''The method items(), which returns a list of key-value pairs.'''

for value in info.keys():
    print(value.title())

for value in info.values():
    print(value.title())

for value in info:  #return key values 
    print(value.title())  
