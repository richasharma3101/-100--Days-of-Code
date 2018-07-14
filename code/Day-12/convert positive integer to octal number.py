def octal(num):
    if num>7:
        octal(num/8)
    print(num%8,end=" ")
num=int(input("Enter a integer:"))
print("\n The octal number of %d integer is: " %num,end=" ")
octal(num)
