class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def my_start(self):
        print("The car is started.")

    def my_stop(self):
        print("The car is stopped.")

    def my_display_info(self):
        print(f"Car Information:\nColor: {self.color}\nType: {self.car_type}\nYear: {self.year}")

my_car = Car("Black", "BMW", 2026)

my_car.my_display_info()




