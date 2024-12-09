# Representan la manera de establecer flujos de ejecución de nuestro código

# Si se cumple una condición yo ejecuto lo que tu me digas que esta dentro del condicional

my_condition = False  # No se imprime el if

if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecición continúa") 

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

print("La ejecición continúa") 


if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else: 
    print("Es menor o igual que 10 o mayor o igual que 20")


if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: 
    print("Es igual a 25")
else: 
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

my_string = "" # Es igual a False

if my_string: 
    print("Mi cadena de texto es vacía")

my_string = "Mi cadena de texto" # Es igual a True

if  not my_string: 
    print("Mi cadena de texto no  es vacía")

my_string = "" # Es igual a False

if  not my_string: # Hace que my_string sea True
    print("Mi cadena de texto no  es vacía")