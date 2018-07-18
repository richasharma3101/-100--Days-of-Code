def binarySearch(alist,item):
    first=0
    last=len(alist)-1

    while first<=last :
        mid=(first+last)//2
        if alist[mid]==item:
            return mid
        else:
            if item<alist[mid]:
                last=mid-1
            else:
                first=mid+1
        
    return None
a=[0,1,2,8,13,17,19,32,42]
item=int(input("Enter the element you want to search"))
n=binarySearch(a,item)
if(n==None):
    print("Not found")
else:
    print("Item Found at location ",n)

