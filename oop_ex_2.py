class FruitInfo:
    fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    fruit_price_list = [200, 80, 70, 110, 60]


    @staticmethod
    def get_fruit_price(fruit_name):
        f_n_l = FruitInfo.get_fruit_name_list()
        if fruit_name in f_n_l:
            for index, fruit in enumerate(f_n_l):
                if fruit == fruit_name:
                    return FruitInfo.get_fruit_price_list()[index]
        return -1

    @staticmethod
    def get_fruit_name_list():
      
       return FruitInfo.fruit_name_list
       

    @staticmethod
    def get_fruit_price_list():
       
        return FruitInfo.fruit_price_list


class Purchase:

    counter = 101

    def __init__ (self, customer, fruit_name, quantity):
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__purchase_id = "P"
        

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_quantity(self):
        return self.__quantity
    
    def get_fruit_name(self):
        return self.__fruit_name

    def calculate_price(self):
        price_kg_fruit =  FruitInfo.get_fruit_price(self.__fruit_name)
        
        if price_kg_fruit == -1:
            return -1
        else:
            quantity = self.get_quantity() /1000
            total = price_kg_fruit * quantity
            discount = 0
            if quantity > 1 and self.__fruit_name == "Apple":
                discount += 2
            if self.__fruit_name == "Sweet Lime" and quantity >= 5 : 
                discount += 5
            
            total = total - total * discount / 100
            if self.get_customer().get_cust_type() == "wholesale":
                total = total - total * 0.1

            self.__purchase_id = "P" + str(Purchase.counter)
            Purchase.counter += 1

            
            return total

class Customer:

    def __init__ (self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type


    def get_customer_name(self):
        return self.__customer_name


    def get_cust_type(self):
        return self.__cust_type


        
cus1 = Customer("Tom", "regular")
cus2 = Customer("Krista", "wholesale")

purchase1 = Purchase(cus1, "Apple", 2000)
calc_price = purchase1.calculate_price()

purchase2 = Purchase(cus2, "Apple", 2000)
calc_price2 = purchase2.calculate_price()

print(f"the calculated price for customer 1 who bought an {purchase1.get_fruit_name()} is {calc_price} and the purchase id is {purchase1.get_purchase_id()}")
print(f"the calculated price for customer 2 an {purchase2.get_fruit_name()} is {calc_price2} and the purchase id is {purchase2.get_purchase_id()}")