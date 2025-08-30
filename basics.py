
#math operations

n1=10
n2=20
print(n1+n2) # same (-,*,/)
print('next inuput below')

#mini calculator

a=int(input())
b=int(input())
operation=input('Add/Sub/Mul/Div :')

if(operation=='Add'):
         print(a+b)
elif(operation=='Sub'):
         print(a-b)
elif(operation=='Mul'):
         print(a*b)
elif(operation=='Div'):
         print(a/b)

else:
    print('try again')


#number divisible by both 3 and 5

num=int(input())
if (num %3 and num %5==0):
    print(num,'is dividible by both 3 and 5')
else:
    print('it is not dividible by 3 and 5')


#Student score

Score=int(input('Enter your percentage :'))
if(Score>=70):
    name=input('Enter your name')
    department=input('enter your department')
    print('you are eligible')

else:
    print('you are not eligible')


#Loan amount

salary=int(input('Enter the Salary amount: '))
age=int(input('enter your age:'))
if(salary>25000 or age<=25):
    loan=int(input('Enter the loan amount:'))
    if(loan >50000):
        print('loan not available')
    else:
        print('loan available')
else:
    print('Not eligibble for loan')



#Student total marks
mark1=int(input('Enter mark 1:'))
mark2=int(input('Enter mark 2:'))
mark3=int(input('Enter mark 3:'))
mark4=int(input('Enter mark 4:'))
mark5=int(input('Enter mark 5:'))

totalmark=mark1+mark2+mark3+mark4+mark5
average=totalmark/5
print('total mark is:',totalmark,'and the average is',average)
if (average<35):
    print('Additional class required')
else:
    print('You are ready to go')































    
