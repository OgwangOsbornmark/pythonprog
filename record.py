from products import Product
from customer import Customer

product1 = Product("bicycle","BC20")
product2 = Product("car toy", "CT29")
product3 = Product("flash disk", "FD90")

customer1 = Customer("peter","CA102", True, 9000, "bicycle", "cs20")
customer2 = Customer("sam", "CT209",False, 500000, "flash disk","cm10")
custmer3 = Customer("osborne","OSB20",True, 300000, "car toy","dr15")


print(f'\ncustomer1\n{customer1}\n\ncustomer2\n{customer2}\n\ncustomer3\n{custmer3}')