import json
import pickle

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Serializer:

    def __init__(self, instance) -> None:
        self.instance = instance

    def to_json(self):
        return json.dumps(self.instance.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.instance.__dict__)

class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __getattr__(self, attr):
        """ metodo utilizado para acceder a un atributo que no esta definido en el objeto
         el atributo que le estaria pasando en un llamado seria el to_json()
           """
        return getattr(Serializer(self), attr) # accede a los metodos de la clase serializer

employee_1 = Employee("anibal", 23, 70000)
print(employee_1.to_json())
