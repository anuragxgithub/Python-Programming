'''
5. Polymorphism
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, 
         but with different behaviors.

'''
class Car:
    # NOTE: __init__ is the constructor (this method is called automatically
    #       whenever a new object of the class is created).
    def __init__(self, brand, model):   # 'brand' and 'model' is the attributes of Car class
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_car2 = Car("Tata", "Safari")
print(my_car2.brand)

e_car = ElectricCar("Tesla", "Model Y", "200kWh")

print(my_car.fuel_type())
print(e_car.fuel_type())
