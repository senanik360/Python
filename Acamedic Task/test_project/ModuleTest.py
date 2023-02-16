import module1

check=module1.makeList(5)

module1.ls(check,2)
ch=module1.bs(check,2)
if ch != -1:  
    print("Element is found")  
else:  
    print("Element is not found")  