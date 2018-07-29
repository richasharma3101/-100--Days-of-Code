def find_len(list):
    length=len(list)
    list.sort()
    print("Largest element is:", list[length-1])
    print("Smallest element is:", list[0])
    print("Second Largest element is:", list[length-2])
    print("Second Smallest element is:", list[1])
list=[12, 45, 2, 41, 31, 10, 8, 6, 4, 1 ,5,45,13,44,76]
Largest = find_len(list)
