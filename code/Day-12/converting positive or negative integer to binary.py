n=int(input("Enter a number"))
a,flag=[],1
if n<0:
    n*=-1
    flag=0
while n>0:
    a.append(n%2)
    n=int(n/2)
if flag==0:
    a.append(1)
else:
    a.append(0)
print(a[::-1])
