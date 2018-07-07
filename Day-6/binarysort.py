def sort(arr,n):
    #count the no. of 0s
    count=0
    for i in  range(0,n):
        if(arr[i]==0):
            count=count+1
    # Loop fills the arr with 0 until count
    for i in range(0,count):
        arr[i]=0
    for i in range(count,n):#remaining space fills with 1's
        arr[i]=1
def print_arr(arr,n):
    print("Array after sorting is  ",end="")
    for i in range(0,n):
        print(arr[i] , end="")
arr=[1, 0, 1, 1, 1, 0, 0, 1, 0]
n=len(arr)
sort(arr,n)
print_arr(arr,n)


        

