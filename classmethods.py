class laptop:
    chargertype='ctype'
    
    def __init__(self):
        

        self.brand=''
        self.price=34

    def setprice(self,price):
        self.price=price


    def getprice(self):
        print(self.price)

    @classmethod
    def chargertype(cls):
        cls.chargertype='btype'
        print('charger type is b')


hp=laptop()
hp.setprice=(2000)
hp.getprice()
laptop.chargertype()
