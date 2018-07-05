def sum(a,b):
    return a + b;
def sub(a,b):
    return a - b;
def mul(a,b):
    return a * b;
def div(a,b):
    return a / b;
print("Select Operation")
print("1.Sum")
print("2.Sub")
print("3.Mul")
print("4.Div")
select= input("Enter choice(1/2/3/4):")
num1=int(input("Enter first number:"))
num2=int(input("Enter Second number:"))
if select=='1':
     print(num1,"+",num2,"=",sum(num1,num2))
elif select=='2':
     print(num1,"-",num2,"=",sub(num1,num2))
elif select=='3':
     print(num1,"*",num2,"=",mul(num1,num2))
elif select=='4':
     print(num1,"/",num2,"=",div(num1,num2))
else:
    print("invalid input")
