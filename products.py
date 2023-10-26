class Product:
    def __init__(self,product_name,product_id):
        self.product_name = product_name
        self.product_id = product_id
    def set_product_name(self,product_name):
       self.product_name = product_name        

    def get_product_name(self):
        return self.product_name  
    
    def set_product_id(self,product_id):
       self.product_id = product_id        

    def get_product_id(self):
        return self.product_id 
    
    def __str__(self):
        return f'\nProductid: {self.get_product_id()}\nProductname: {self.get_product_name()}'
product1 = Product("casasva","cas123")    
print(product1)