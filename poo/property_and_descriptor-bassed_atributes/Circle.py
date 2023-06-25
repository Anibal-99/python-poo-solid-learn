import math

class Circle:

    class_attr=100

    # constructor del objeto, establece los valores iniciales para tus atributos
    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius**2)

    def method(self):
        print(f'Class attribute:{self.class_attr}')
        print(f'Instance attribute: {self.radius}')


print(Circle.class_attr)
print(Circle.__dict__)
print(Circle.__dict__["class_attr"])
circle_1=Circle(30)
print(circle_1)
print(circle_1.calculate_area())

circle_2=Circle(200)

print(circle_2.radius)
print(circle_2.method())
print(circle_2.__dict__)
circle_2.__dict__["radius"]==3000
print(circle_2.__dict__)
print(circle_2.radius)
