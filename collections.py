a=(1,2,3,4,5) #list changeable,allow dulicate
b=[1,2,3,4,5]  #tuple unchangeable ordered, allow duplicate
c={1,2,3,4,5}  #set unchangeable,not allow duplicate
d={'name':'mega'} #dictonary changleable ,no duplicate
print(type(a))
print(type(b))
print(type(c))
print(d)

b.append(6)
print(b)
