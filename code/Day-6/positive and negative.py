a=[int(i) for i in input("Enter the number").strip().split()]
subarray=[[]]
print("Original Array is :",str(a))

for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        sub_element=a[i:j]
        subarray.append(sub_element)
print("Subarray having sum 0")
for sub  in subarray:
    sum=0
    for l in range(len(sub)):
        sum=sum+sub[l]
    if(sum==0 and len(sub)>0):
        print(sub)
