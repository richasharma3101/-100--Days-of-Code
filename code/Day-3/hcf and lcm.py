from math import gcd
arraylist=list()
num=int(input("How many numbers you want to enter:"))
print('Enter numbers:')
for i in range(int(num)):
    n=input()
    arraylist.append(int(n))
print('Numbers :',arraylist)
lcm=1
for i in arraylist[0:]:
    lcm=int(lcm*i/gcd(lcm,i))
def find_gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
num1=arraylist[0]
num2=arraylist[1]
gcd=find_gcd(num1,num2)
for i in range(2,len(arraylist)):
    gcd=find_gcd(gcd,arraylist[i])
print("Hcf is:",gcd)
print("Lcm is:",lcm)
