a=[]
num=int(input("Enter a number"))
while num>1:
    a.append(num%2)
    num=int(num/2)
a.append(1)
print("Binary of a number is:",a[::-1])
