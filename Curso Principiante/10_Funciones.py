# Funciones

# Se utilizan para resolver 2 problemas, primero encapsular una logica muy concreta, es decir, resolver un problema concreto; en segundo, evitar errores ya que siempre que querramos resolver un prblema llamaremos a la funcion que lo resuelve evitando duplicar código

def my_function (): # Definimos a la función
    print("Esto es una función")

my_function ()  # Llamamos a la función

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values (5, 9)

print("")

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")  #Sin la f imprimiria tal cual la cadena de texto como la anotamos, por lo que la necesitamos para que imprima los valores que le vamos a dar a las variables.

print_name("Mariano", "Martinez")


def print_name_for_defoult (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_for_defoult("Mariano", "Martinez")

def print_texts (*text):
    print(text)

print_texts("{name}", "{surname}", "{alias}")

