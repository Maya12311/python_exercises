class Apparel:
    counter = 100

    def __init__(self, price, item_type):
        self.__price = price
        self.__item_type = item_type
        Apparel.counter += 1
        if item_type.lower() == "cotton":
            self.__item_id = 'C' + str(Apparel.counter)
        else:
            self.__item_id = 'S' + str(Apparel.counter)

    def calculate_price(self):
        service_tax = 5
        price = self.get_price()
        self.set_price(price+ price*service_tax/100)
        return self.get_price()
    
    def get_item_id(self):
        return self.__item_id
    
    def get_price(self):
        return self.__price
    
    def get_item_type(self):
        return self.__item_type

    def set_price(self, price):
        self.__price = price
        

    

class Cotton(Apparel):

    def __init__(self, price, discount):
        super().__init__(price, "Cotton")
        self.__discount = discount

    
    def calculate_price(self):
        
        super().calculate_price()
        price_with_service_tax = self.get_price()
        final = price_with_service_tax - price_with_service_tax* self.get_discount()/100

        final_with_vat = final + final * 5/100
        self.set_price(final_with_vat)

        return self.get_price()
    
    def get_discount(self):
        return self.__discount
        

class Silk(Apparel):

    def __init__(self, price):
        super().__init__(price, "Silk")

    
    def calculate_price(self):
        super().calculate_price()
        price_with_service_tax =  self.get_price()
        points = 0
        if price_with_service_tax > 10000: 
            points+= 10

        else:
            points+= 3
        
        self.__points = points

        self.set_price(price_with_service_tax + price_with_service_tax * 10/100)

        return self.get_price()
    
    def get_points(self):
        return self.__points




cotton_apparel = Cotton(1000, 10)
print(cotton_apparel.calculate_price())
print()

silk_apparel = Silk(10001)
print(silk_apparel.calculate_price())
print(silk_apparel.get_points())