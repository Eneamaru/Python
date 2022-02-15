class Car:
    speed = 0
    color = ''
    name = ''
    is_police = True

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f'{self.name} turn {direction}')

    def show_speed(self):
        print(f'current speed {self.name} {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print(f'current speed {self.speed}. speeding!')
        else:
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print(f'current speed {self.speed}. speeding!')
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police


car_1 = TownCar(0, 'white', 'Lada')
car_1.go()
car_1.show_speed()
car_1.speed = 100
car_1.show_speed()
car_1.turn('right')
car_1.stop()

car_2 = SportCar(0, 'red', 'McLaren')
car_2.go()
car_2.show_speed()
car_2.speed = 250
car_2.show_speed()
car_2.turn('left')
car_2.stop()

car_3 = WorkCar(0, 'black', 'Toyota Hilux')
car_3.go()
car_3.show_speed()
car_3.speed = 100
car_3.show_speed()
car_3.turn('right')
car_3.stop()

car_4 = PoliceCar(0, 'blue', 'Corvette')
car_4.go()
car_4.show_speed()
car_4.speed = 200
car_4.show_speed()
car_4.turn('left')
car_4.stop()
