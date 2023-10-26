class Payment:
    #attributes of class
    amount_paid = 0
    balance = 0
    credit = 0

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"amount_paid {self.amount}"
        
    #creating function to compuet price using an abstract method
    
    @classmethod
    def set_amount_paid(cls,product1,product2,product3):
        from customer import Customer
        if Customer == True:
            cls.amount_paid = 0.5*(product1+product2+product3)
        else:
            cls.amount_paid = product1+product2+product3

    @classmethod
    def get_amount_paid(cls):
        return cls.amount_paid
    
 
    
    def get_balance(self):
        if self.amount > self.amount_paid:
            return  self.amount-self.amount_paid

    def get_credit(self):
        if self.amount < self.amount_paid:
            return self.amount_paid-self.amount
        
    def __str__(self):
        return f"Amount_paid: {self.amount}\nBalance: {self.get_balance()}\nCredit: {self.get_credit()}"
    
#Payment.set_amount_paid(10000,20000,40000)
#print(Payment.get_amount_paid)

payment1 = Payment(10000)
print(payment1.get_balance())
print(payment1.get_credit())

payment2 = Payment(20000)
print(payment2.get_balance())
print(payment2.get_credit)