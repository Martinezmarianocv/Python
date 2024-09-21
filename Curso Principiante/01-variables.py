# Variables

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 4
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False 
print(my_bool_variable)

# Concatenación de variables en un print

print(my_variable, my_int_to_str_variable, my_bool_variable)
print("hola", ",", "Mundo", "!")
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema

print(len(my_int_to_str_variable)) # len cuenta los caracteres
print(len(my_variable)) # len cuenta los caracteres

# Variables en una sola línea

name, surname, alias, age = "Mariano", "Martinez", "Nanodev", 23
print("Me llamo", name, surname,",", "mi alias es", alias, "y mi edad es de", age)

# Inputs

name = input("What is your name? ")
age = input("How old are you? ")

print(name)
print(age)

# Cambiamos su tipo de dato a las variables

name = 23
age = "Mariano"

print(name)
print(age)

# ¿Forzamos el tipo?

address: str  = "Mi dirección"
address = 32
print(address)