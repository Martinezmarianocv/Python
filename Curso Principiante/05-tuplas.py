# Una tupla es un conjunto de valores CONSTANTES, no se pueden cambiar los datos ya dados tal como con las variables o las listas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1.70, "Mariano", "Martinez")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Martinez")) # Cuenta la cantidad de elementos dados, en la tupla

print(my_tuple.index("Martinez")) # Dice en que posicion esta el elemento dado

''' my_tuple[1] = 1.73   no se pueden cambiar los valores ya dados
print(my_tuple)          a las tuplas '''

my_other_tuple = (34, 23, 54, 65)
print(my_other_tuple)

print(my_tuple + my_other_tuple) # Se pueden sumar las tuplas

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[2:6]) # Esto me devuelve los valores que estan entre la posicion 2 y la 6 dentro de la tupla

my_tuple = list(my_tuple) # Cambiamos de tupla a lista
print(type(my_tuple))

my_tuple[3] = "NanoDev"
my_tuple.insert(1, "Cian")
print(my_tuple)

my_tuple = tuple(my_tuple) # Cambiamos de lista a tupla
print(type(my_tuple))

''' del my_tuple  Elimina la variable completa y no debemos hacerlo, es un ERROR
print(my_tuple)   NameError: name 'my_tuple' is not defined '''