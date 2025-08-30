
#for loop

for i in 'apple':
    print(i)

#print range   
for i in range(5):
    print(i)
    
#print a certain range

for i in range(1,10):
    print(i)

#print a range with custom 
for i in range(1,11,2):   #increase by 2
    print(i)

#print a range with a string
for i in range(1,10):
    print('python')


#print tables using for loop
for i in range(0,11):
    print(i,'x3',i*3)


#Example 1 get input of a,b and print the numbers between them
a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)

#Example 2 print the even number between 1 to 10
for i in range(1,11):
    if(i%2==0):
        print(i)

#Example 3 print the odd number between 1 to 10
for i in range(1,11):
    if(i%2!=0):
        print(i)



#Example 4 count the total number of odd numbers between 1 to 10
count=0
for i in range(0,11):
    if(i%2!=0):
        count=count+1
print(count)


#Example 5 count the total numbers between 1 to 10 which are divisible by 3 and 5

count=0
for i in range(1,31):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)


#Example 6 write a program to compute and sum the first 5 natural numbers

sum=0
for i in range(1,6):
    sum=sum+i
print(sum)


#Example-1[list]  10 numbers fom user input using list and their sum
a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)

#Example-2 input =4 ,output=1,2,3,4
sum=0
a=int(input())
for i in range(1,a+1):
    print(i)
    sum=sum+i
print(sum)


#Example-3 display the cube of the number upto the integer

a=int(input())
for i in range(1,a+1):
   print(i,'and the cube is ',i*i*i)



#nested loop
for i in range(1,3):
    print('week:',i)
    for j in range(1,4):
        print('day',j)


#pattern printing right triangle

for i in range(6):
    print()
    for j in range(1,i+1):
        print('*',end='')

#pattern printing square
        
n=5
for i in range(n):
    print('*'*n)

#for loop when the iterations are  known
#While loop when the number of  iterations known

#print the number 1 to 5 using while loop
i=1
while(i<=5):
    print(i)
    i=i+1

#print  10,20,30,40....200
i=10
while(i<=200):
    print(i)
    i=i+10
  
#first 10 natural numbers in reverse order with or without user input

i=int(input())
while(i>0):
    print(i)
    i=i-1
  
#write a program to find the factorial of a number
i=int(input())
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)
     














        
        
