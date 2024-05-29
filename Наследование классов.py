class Car:
    def __init__(self):
        self.price = 1000000
        self.horse_powers = 100

class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price =1200000
        self.horse_powers = 120

class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1280000
        self.horse_powers = 140

nissan = Nissan()
kia = Kia()
print(kia.price)
print(kia.horse_powers)
print(nissan.price)
print(nissan.horse_powers)
