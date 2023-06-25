"""
    Atributos dinamicos de clases e instancias
    -------------------------------------------
    Si tenemos una clase que no sabemos que atributos le van a llegar podemos hacer lo siguiente
"""

class Record:
    pass

john = {
    "name": "john Doe",
    "position": "Python developer"
}

john_record = Record()

# field es el atributo del objeto john_record
# value es el valor que tendra el atributo (field)

for field, value in john.items():
    setattr(john_record, field, value)

print(john_record.name)
print(john_record.position)


# Tambien podemos agregarle un metodo

def __init__(self,name, position):
    self.name=name
    self.position=position

Record.__init__=__init__

jey = Record("joaquin", "backend")
print(jey.name)
print(jey.position)
