def insertionSort(a,n):
    for i in range(1,n):
       key=a[i]
       j=i-1
       while j>=0 and key<a[j]:
           a[j+1]=a[j]
           j=j-1
       a[j+1]=key
a=[64,34,25,12,22,11,90]
n=len(a)
insertionSort(a,n)
print("Sorted array is")
for i in range (n):
    print(a[i],end=" ")
