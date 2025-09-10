'''
3. Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
'''

class Car:
    # NOTE: __init__ is the constructor (this method is called automatically
    #       whenever a new object of the class is created).
    def __init__(self, brand, model):   # 'brand' and 'model' is the attributes of Car class
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):             # IHERITANCE
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize



my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_car2 = Car("Tata", "Safari")
print(my_car2.brand)

print(my_car.full_name())
print(my_car2.full_name())
    
# INHERITANCE
e_car = ElectricCar("Tesla", "Model Y", "200kWh")
print(e_car.full_name())
print(e_car.batterySize)