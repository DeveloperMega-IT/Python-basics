'''
#Sum of Digits
#Take a number (e.g., 1234) and print the sum of its digits (1+2+3+4 = 10).

num=int(input())
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

#Swap Numbers
#Swap two numbers without using a third variable.
a=int(input()
b=int(input()
a,b=b,a
print(a)



#Largest of Three
#Take three numbers as input and print the largest one.
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)

else:
    print('The largest one is:',c)


#Fibonacci Series

# Program to print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))  # user input for length

a, b = 0, 1  # first two numbers
print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")  # print current number
    a, b = b, a + b    # update values: next = sum of previous two


# Program to print a right triangle pattern using *

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    # "*" * i will repeat * i times
    print("*" * i)
'''

#Factorial Function

def factorial(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result

num=int(input())
print(factorial(num))

































    
