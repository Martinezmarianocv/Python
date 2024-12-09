# Bucles / Loops / Ciclos 

# Sirve para iterar (Repetir el mismo códogo varias veces)

# While : Debemos pasarle una condición, mientras que haya una expresión es verdadero

my_condition = 0

while my_condition < 10: # Se ejecuta hasta que my_condition sea el numero más cercano a 10
    print(my_condition)
    my_condition += 2
if my_condition == 10: 
    print("Mi condición es igual que 10")
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución") 
        break # Se usa para detener el bucle una vez se cumpla la condición anterior
    print("Mi condición es menor que 20")


print("")

print("For")

# For : Debe cumplir una condición e itera un grupo de elementos. Hace que un codigo se repita tantas veces como elementos tengamos iterables. Cada vez que repite el codigo tiene acceso al elemento siguiente de la lista/set/tupla/diccionario.

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print("")

my_set = {"Martinez", "Mariano", 23}

print("")

for element in my_set:
    print(element)

print("")

my_tuple = (23, 1.70, "Mariano", "Martinez")

for element in my_tuple:
    print(element)

print("")

my_dict = {"Nombre":"Mariano", "Apellido":"Martinez", "Edad":23, 1:"Python"} 

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # Se detiene la ejecución del bucle en este punto volviendo al for.
else:
    print("Mi bucle for a terminado")

print("")
