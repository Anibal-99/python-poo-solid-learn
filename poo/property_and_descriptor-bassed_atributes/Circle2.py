import math

class CircleDos:

    class_attr=100

    # constructor del objeto, establece los valores iniciales para tus atributos
    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    def radius(self): # devolvera el valor del atributo
        return self._radius

    @radius.setter
    def radius(self, value) -> int:
        if not isinstance(value, int | float) or value <=0:
            raise ValueError("positive number expected")
        self._radius=value


    def calculate_area(self):
        return round(math.pi * self.radius**2)

    def method(self):
        print(f'Class attribute:{self.class_attr}')
        print(f'Instance attribute: {self.radius}')


circle = CircleDos(100)
print(circle.radius)
circle.radius=300
print(circle.radius)
circle.radius=0
print(circle.radius)
