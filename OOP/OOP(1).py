class Car():
    def __init__(self, brand_car, model_car ,year):
        self.brand_car = brand_car
        self.model_car = model_car
        self.year = year
    def displayInfo(self):
        return f"Марка машины = {self.brand_car}, Модель = {self.model_car}, Год выпуска = {self.year}"

car = Car("Nissan", "SKYLINE", "2000")
print(car.displayInfo())