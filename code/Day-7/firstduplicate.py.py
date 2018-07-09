arr=[int(x) for  x in input("Enter the number seperated by space= ").strip().split()]
for x in range(len(arr)):
    if arr[x] in arr[x+1:]:
        print("First duplicate array ",arr[x])
        break
