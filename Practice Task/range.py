evenNumber=list(range(2,11,2))

print(evenNumber)


src=[]
print(src)
for value in range(1,11):
    src.append(value**2);
print(src)



src=[]
print(src)
src=[value**2 for value in range(1,11)]

print(src)

print("Minimum ",min(src))
print("Maximum ",max(src))
print("Sum ",sum(src))