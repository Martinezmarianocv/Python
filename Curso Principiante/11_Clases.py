# Classes

# Las classes nos sirven para identificar algo que tenga logica con la misma clase y nos va a servir para identificar ese algo durante todo el programa. Podemos definir una classe persona y su lógica debe responder a lo que una persona es.

class EmptyPerson: # Las classes se escriben con CamelCase
    pass # Sirve para que la classe se ejecute sin que tenga nada dentro.

print(EmptyPerson)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("Mariano", "Martinez")
print(my_person.name)
print(my_person.surname)

# También podemos escribirlo print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self, name, surname, alias = "sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person("Mariano", "Martinez")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Sofía", "Flogliacco", "Sofifrog")
print(my_other_person.full_name)
my_other_person.walk()