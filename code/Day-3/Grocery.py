items=[]
amounts=[]
flag =False
file= open('grocery.txt','w+')
n=int(input("Number of items:"))
print('Enter the item with their amount')
for i in range(0,n):
      item=str(input())
      items.append(item)
      amount=str(input())
      amounts.append(amount)
      file.write(items[i]+'=>'+str(amounts[i])+'\n')
file.close()

file= open('grocery.txt','r')
if(file.mode=='r'):
      f1=file.readlines()
search=str(input('Enter the item you want to search:'))
for i in range(0,len(f1)):
    if search in f1[i]:
        index=i
        flag=True
        break;
if(flag):#if item found in file
      print(str(amounts[index])+'\n')
else:
      print('item not found in file')
file.close()
      
      
