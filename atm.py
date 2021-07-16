class Atm():
    def __init__(self,amount=0):
        self.amount = amount
    
    def add_amount(self,add_a):
        self.a = add_a
        self.amount += self.a
        print("Amount has been added")
    
    def withdrow_amount(self,with_a):
        self.w = with_a
        if self.w > self.amount:
            print("Insufficent Amount")
        else:
            self.amount -= self.w
            print("Amount {} has been withdrow".format(self.w))
    
    def display_amount(self):   
        print("Total amount {}".format(self.amount))

c = Atm()
add = int(input("Enter Ammount to add : "))
c.add_amount(add)
c.display_amount()
with_drow = int(input("Enter Ammount to withdraw : "))
c.withdrow_amount(with_drow)
c.display_amount()