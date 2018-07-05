def fact(n):
    if n==1:
        return (n)
    elif n<0:
        print("Factorial does not exist")
    elif n==0:
        return (1)
    else:
        return (n*fact(n-1))
n = int(input("Enter number:"))
print("factorial is:")
print(fact(n))
  
