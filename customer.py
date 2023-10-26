class Customer:
#definning variables of the class
    def __init__(self, name, identification_number, is_regular_customer, payment_made, product_ordered,product_id):
        from payment import Payment
        from products import Product
        Payment.set_amount_paid(20000,30000,100000)
        self.name = name
        self.identification_number = identification_number
        self.is_regular_custome = is_regular_customer
        self.payment_made = Payment(payment_made)
        self.product_ordered = Product(product_ordered,product_id)

        #creating function to display customer_name and identification number
    def __str__(self):
        return f"Customer name:{self.name}\nCustomer identfication:{self.identification_number}\ncustomer payment{self.payment_made}\nCustomer Product{self.product_ordered}"
    
    #craeting an object of a class customer
#customer = Customer(input("Enter cutomer name: "), input("Enter identification number:"))
#print(customer)