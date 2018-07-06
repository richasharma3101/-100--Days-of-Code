import random as r
def quesans(count,score):
    count=count+1
    num1=int(r.randint(1,999))
    num2=int(r.randint(1,999))
    operation=int(r.randint(1,2))
    if(operation==1):
        symbol='+'
        result=int(num1+num2)
    elif(operation==2):
        symbol='-'
        result=int(num1-num2)
    print('question'+str(count)+'=>'+str(num1)+symbol+str(num2))
    answer=int(input('Answer'))
    if(answer==result):
        print('Your answer is correct')
        score=score+1
        print('Total correct answer:',score)
        quesans(count,score)
    else:
        print('Incorrect answer')
        print('Total correct answer:',score)
        quesans(count,score)
    return count
count=0
score=0
quesans(count,score)
