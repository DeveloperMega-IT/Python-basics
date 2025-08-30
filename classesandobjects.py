
#example 1 

class goa:
    name=''
    drink=''
    def party(self):
        print('Enjoy the party')
    def beach(self):
        print('Enjoy the beach')

mega=goa()
ashok=goa()
ashok.drink='yes'
mega.name='priya'
print(mega.name)
print('drink',ashok.drink)

#Example 2

class laptop:
    price=''
    processor=''
    ram=''

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=input()
dell.price='300'
lenovo.price='300'

dell.processor=input()

print(hp.price)
print('processor for dell is',dell.processor)

#example 3
class student:
    def __init__(self):
        self.name=input()
        self.regnum=int(input())
        
    def display(self):
            print(self.name)
            print(self.regnum)
s1=student()
# print(s1.name)
# print(s1.regnum)

s1.display()


#example 4
class fruit:
    fruit=['apple','mango','grapes','orange']
    for i in fruit:
        print(i)
          
    def __init__(self):
        colour=''


a=fruit()
a.colour='red'
print(a.colour)

class f2:
    def __init__(self,col):
        self.colour=col


apple=f2("red")
print(apple.colour)


#example 5

class phone():
    charger='c-type' #class variable
    def __init__(self,brand,price):
         self.brand=brand #instance variable
         self.price=price
    def display(self):
        print(self.brand)
        print(self.price)
        print(self.charger)
phone.charger='btype'
samsung=phone('samsung','30000')
lava=phone('lava','4000')
nokia=phone('moto','1000')

samsung.display()
nokia.display()
lava.display()

        
        





