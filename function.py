
#math operations using functions

def maths():
    print('Add,Sub,Mul,Div :')
    a=int(input())
    b=int(input())
    print(a+b,a-b,a*b,a/b)
maths()


#find even or odd

def evenorodd(num):
    if(num%2==0):
        print("Even")
    else:
        print('Odd')
evenorodd(10)


#print the range between a and b

def getrange(a,b):
    for i in range(a,b+1):
        print(i)

getrange(1,10)



#username and password validation
S_name = 'mega'
passw = 'passwS'  # You should define a password value for validation

uname = input('Enter the username: ')
password = input('Enter the password: ')

def validate():
    if uname == S_name and password == passw:
        print('Login correct')
    else:
        print('Invalid credentials')

validate()

#(a+b)*c
a=int(input())
b=int(input())
c=int(input())
def sum(n1,n2,n3):
    n1+n2
    added=n1+n2
    mul=added*c
    print(mul)

sum(a,b,c)
   






















               
