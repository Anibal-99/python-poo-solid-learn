from datetime import datetime

class Employee:

    companny = 'google'

    def __init__(self, name, surname, birth_date) -> None:
        self.name = name
        self.surname = surname
        self.birth_date = birth_date


    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        """convierte el string que le pasas a un datetime, le formato es year-month-day"""
        self._birth_date = datetime.fromisoformat(value)
        return self._birth_date


    # metodo de instancia, porque toma la instancia actual, self
    def compute_age(self):
        """ calcula la fecha de cumpleañoas par a el año actual  devuelve los años que tiene el empleado"""

        today = datetime.today()
        age = today.year - self._birth_date.year

        birthday = datetime(today.year, self.birth_date.month, self.birth_date.day)

        if today < birthday:
            age -= 1

        return age

    @classmethod
    def from_dict(cls, data_dict):
        """ toma un diccionaria de datos de un empleado y crea una instancia de employee con el argumento cls y luego desempaqueta el diccionario de datos """
        return cls(**data_dict)


    def __str__(self) -> str:
        return f'{self.name} is {self.compute_age()} years old'

    def __repr__(self) -> str:
        """ devuelve una cadena que permitira crear de nuevo el objeto actual """
        return (
            f"{type(self).__name__},"
            f"name={self.name},"
            f"birth_date={self.birth_date.strftime('%Y-%m-%d')}"
        )


employee_1 = Employee('Anibal','Alvarez','1999-12-04')
print(employee_1.companny)
print(employee_1.compute_age())
print(employee_1)

""" crea un diccnario con los datos del empleado, luego crea un nuevo objeto con el metodo de clase from_dict y le pasa por parametro el diccionario con los datos del nuevo empleado """
employee_2 = {'name': 'Emma', 'surname': 'Alvarez', 'birth_date':'2009-01-07'}
emma = Employee.from_dict(employee_2)
print(emma)
