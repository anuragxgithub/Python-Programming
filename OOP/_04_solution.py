'''
4. Encapsulation
Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.


Background Knowledge:
bundling data (attributes) and the methods that operate on that data into a single unit
called a class, while restricting direct access to the data to control its use.
Access modifiers like 'private' and 'public', and methods called 'getters' and 'setters', are used to implement
encapsulation.
'''
class Car:
    # NOTE: __init__ is the constructor (this method is called automatically
    #       whenever a new object of the class is created).
    def __init__(self, brand, model):   # 'brand' and 'model' is the attributes of Car class
        self.__brand = brand      # we use __ before the attribute to make it private
        self.model = model

    def full_name(self):
        pass
        # return f"{self.brand} {self.model}"
    
    def get_brand(self):                    # this is getter function (used to retrieve the value of provate private or protected variable/attribute)
        return self.__brand + " !"


my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
print(my_car.model)

my_car2 = Car("Tata", "Safari")
# print(my_car2.brand)

print(my_car.full_name())
print(my_car2.full_name())
    
# ENCAPSULATION
# print(my_car.brand)  # see now you can't acces the brand attribute directly because it is private
print(my_car.get_brand())



# H.W. : Explore about the setter function