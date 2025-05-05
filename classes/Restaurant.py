class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name  = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant_name is {self.name}.")
        print(f"The restaurant provides {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is open. You can visit now.") 


    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,increment):
        self.number_served += increment    



class IceCreamStand(Restaurant):

    def __init__(self,name,cuisine_type):
        super().__init__(name,cuisine_type)
        self.flavors = ['strawberry', 'vanila']

    def available_flavors(self):
        print(f"the available flavors are {self.flavors[0]} , {self.flavors[1]}")     

my_icecream_stand  = IceCreamStand('PolarBear','icecream')
print(my_icecream_stand.available_flavors())

# my_restaurant = Restaurant("Polar Bear","Ice cream")
# my_restaurant.name
# print(my_restaurant.cuisine_type)      
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()  
# my_restaurant.set_number_served(30)
# print(my_restaurant.number_served)
# my_restaurant.increment_number_served(40)
# print(my_restaurant.number_served)


