class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} {self.color} is starting.....")

car1 = Car("Tesla", "Black")
car2 = Car("BMW","Blue")
car1.start()
car2.start()    