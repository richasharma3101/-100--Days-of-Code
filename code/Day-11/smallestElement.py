def findElement(a,start,end):
    if(start>end):
        return end+1
    if (start!=a[start]):
        return start;
    mid=int((start+end)/2)
    if (a[mid]==mid):
        return findElement(a,mid+1,end)
    return findElement(a,start,mid)
a=[int(i) for i in input("Enter the number").strip().split()]
n=len(a)
print("Smallest missing element is",findElement(a,0,n-1))
