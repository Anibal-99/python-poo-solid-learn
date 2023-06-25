class Vehicle:

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.model = year
        self._started = False

    def start(self) -> str:
        self._started = True
        return f"starting engine"

    def stop(self) -> None:
        self._started = False
        return "stoping engine"

class Car(Vehicle):

    def __init__(self, make, model, year, num_seats) -> None:
        super().__init__(make, model, year) # hace uso del mentod init de la clase padre
        self.num_seats = num_seats

    def drive(self):
        return (f'Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'

class Motorcycle(Vehicle):

    def __init__(self, make, model, year, num_wheels) -> None:
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def ride(self):
       return(f'Riding my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_wheels} wheels'


car_1 = Car("Ford", 'focus', 2022, 4)
print(car_1.start())
print(car_1.drive())

motorcycle_1 = Motorcycle("Honda", "Tornado", 2023, 2)
print(motorcycle_1.ride())
