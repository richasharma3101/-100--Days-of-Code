def pushzeros(arr,n):
    count=0#count for non zero element
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count=count+1
    while count<n:
        arr[count]=0
        count=count+1
arr = [3, 0, 1, 0, 5, 9, 0, 6, 7]
n = len(arr)
pushzeros(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)
