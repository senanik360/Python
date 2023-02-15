def makeList(size):
    arr=[]
    while(size):
        el=int(input())
        arr.append(el)
        size-=1
    return arr

check=makeList(5)

# print(check)

def ls(arr,k):
    print("check ls")
    m=0
    for i in arr:
       m+=1
       if(i==k):
            print("By Linear Search element is Found at index ",m-1)
            break
            

ls(check,2)

def bs(arr, k):  
    arr.sort()
    low = 0  
    high = len(arr) - 1  
    mid = 0  
  
    while low <= high:  
        mid = (high + low) // 2  
  
        if arr[mid] < k:  
            low = mid + 1  
  
        elif arr[mid] > k:  
            high = mid - 1  
  
        else:  
            return mid  
  
    return -1  


ch=bs(check,2)

