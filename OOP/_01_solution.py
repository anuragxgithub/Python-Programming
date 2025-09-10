class Car:
    # NOTE: __init__ is the constructor (this method is called automatically
    #       whenever a new object of the class is created).
    def __init__(self, brand, model):   # 'brand' and 'model' is the attributes of Car class
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_car2 = Car("Tata", "Safari")
print(my_car2.brand)

print(my_car.full_name())
print(my_car2.full_name())
    