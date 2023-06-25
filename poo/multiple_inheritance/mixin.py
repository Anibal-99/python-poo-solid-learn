import json
import pickle

class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class SerializerMixin:
    """ El metodo dumps de json convierte un objeto a un JSON, en este caso le pasamos los datos del objeto que llega (self), y los datos estan el diccionario __dict__ """


    def to_json(self):
        return json.dumps(self.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.__dict__)


class Employee(SerializerMixin, Person):

    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary

employee_1 = Employee("anibal", 23, 70000)

print(employee_1.to_json())
print(employee_1.to_pickle())
