class grandpa():

    def money(self):
        print('money')


class dad(grandpa): #multilevel
    def phone(self):
        print('phone')
        
class land():
    def impot(self):
        print('myland')

class s2(dad,land): #hierarical inheritance
    pass  #creates emptyclass
class s3(dad):
    pass



class mom():
    def laptop(self):
        print('laptop')




class son(dad,land): #multiple
    def car(self):
        print('car')


ram=son()
mani=dad()
j=mom()
raj=grandpa()
ram.car()
mani.money()
son2=s2()
son2.phone()
ram.land()
