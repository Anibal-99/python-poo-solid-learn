class Car:

    def __init__(self, name, speed, started, max_speed) -> None:
        self.name = name
        self.speed = speed
        self.started = started
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, int | float) or value <=0:
            raise ValueError('positive number expected')
        self._speed = value


    def acelerate(self, value):

        if not self.started:
            return 'Car is not started'

        if self.speed + value <= self.max_speed:
            self.speed+=value
        else:
            self.speed = self.max_speed

        return f'Accelerating to {self.speed} km/h...'


car_1= Car('ford', 110, False, 150)
car_1.speed=130
print(car_1.speed)
print(car_1.acelerate(10))
