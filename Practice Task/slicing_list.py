device=['tv','mobile','laptop','desktop','monitor']

print(device)
print(device[0:3])
print(device[1:4])
print(device[:3])
print(device[2:])

for i in device[-3:]:
    print(i.title())


lang="Python"

print(lang[:3])
print(lang[-3:])
print(lang[:])

pang = device 
'''if you assign a list directly into another, it copies the reference.
So, changes in one have impact on other.'''
print(pang)

pang.append("tab")
print(pang)
print(device)

pang = device[:] 
'''here both lists are separated, changes in one does not affect on
other.'''
pang.append("watch")
print(pang)
print(device)

