a=[1,3,5,4,8,10]
for x in range(1,len(a)-1,2):
    if(a[x]<a[x+1]):
        a[x],a[x+1]=a[x+1],a[x]
print(a)
