a=[64,25,12,22,11]
for i in range (len(a)):
    min=i
    for j in range(i+1,len(a)):
        if a[min]>a[j]:
            min=j
    a[i],a[min]=a[min],a[i]
print("Sorted array is")
for i in range (len(a)):
    print(a[i],end=" ")
