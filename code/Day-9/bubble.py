def bubblesort(a,n):
    for i in range(n):
        flag=False
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
        if flag==False:
            break
a=[64,34,25,12,22,11,90]
n=len(a)
bubblesort(a,n)
print("Sorted array is")
for i in range (n):
    print(a[i],end=" ")
