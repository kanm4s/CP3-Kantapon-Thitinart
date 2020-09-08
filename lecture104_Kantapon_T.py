class Customer:
    name = ""
    lastName = ""
    age = 0
    
    def addCart(self):
        print("Added product to",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kantapon"
customer1.lastName = "T."
customer1.addCart()

customer2 = Customer()
customer2.name = "Korn"
customer2.lastName = "P."
customer2.addCart()

customer3 = Customer()
customer3.name = "Beau"
customer3.lastName = "K."
customer3.addCart()

customer4 = Customer()
customer4.name = "Prapan"
customer4.lastName = "T."
customer4.addCart()