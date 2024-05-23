# 1 Определение Простого Класса: Создайте Класс Car с атрибутами brand и year
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.__engine_type = "type"   # 5 приватный атрибут
    def get_engine_type(self):
        return self.__engine_type
# 4 Создание экземпляра: Создайте объект my_car класса Car и выведите его атрибуты
my_car = Car ("Mers", 2021)
print(my_car.brand)
print(my_car.year)
print(my_car.get_engine_type())
# 6 Наследование: Создайте класс ElectricCar, который наследует от класса Car и имеет дополнительный атрибут battery_size
class ElectricCar(Car):
    def __init__(self, brand, year, battery_size):
        Car.__init__(self, brand, year)
        self.battery_size = battery_size
my_car2 = ElectricCar("Mers", 2021, 600)
print(my_car2.battery_size)