'''elements=['anik','cse','10','3.94'];

print(elements)

src=input("Enter element for search : ")
count=0;

for i in elements:
    if(i==src):
        print("Found")
        count+=1
        break;

if(count==0):
    print("Not Found")'''

elements=[15,14,13,12,11,10]
print(elements)
elements.sort()
print(elements)

middle=(1+((len(elements))-1))//2

print(elements[middle])

src=input("Enter element for search [B]: ")
sr = int(src)
#print(type(src)) 

if(sr==elements[middle]):
    print("Found")
