def Input(section):
    n=int(input("Enter the number of students:"))
    m=[[''] for x in range(n)]
    for x in range(n):
        n=0
        print(m)
        while(n<=2):
            k=input("enter{} student {}".format(x+1,section[n]))
            m[x].append(k)
            n+=1
    return m
import csv
with open('Student.csv','w') as newFile:
    section=['Student_Name','Roll No','Marks']
    csv_writer=csv.writer(newFile,delimiter='\t')
    csv_writer.writerow(['Student_Name','Roll No','Marks'])
    m=Input(section)
    for x in range(len(m)):
        csv_writer.writerow(m[x])
