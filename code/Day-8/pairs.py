product,max=1,[0,0,0]
a=[int(i) for i in input("Enter the number").strip().split()]
for i in range(len(a)-1):
    product=a[i]*a[i+1]
    if( max[2]<product):
        max[:]=a[i],a[i+1],product
print(max)
