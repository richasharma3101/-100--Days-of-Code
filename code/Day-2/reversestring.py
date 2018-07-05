def reverse(n):
    str=""
    for i in n:
        str=i + str
    return str
n=input("Enter a string")
print("The original string is:")
print(n)
print("The reverse string is:")
print (reverse(n))
