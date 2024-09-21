my_list = list()    # Ambas maneras sirven para definir una lista
my_other_list = []  # Ambas maneras sirven para definir una lista

print(len(my_list))

my_list = [23, 49, 50, 42]

print(my_list)
print(len(my_list))

my_other_list = [23, 1.70, "Mariano", "Martinez"]
print(my_other_list)
print(len(my_other_list))

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0]) # Para llamar a un elemento de la lista
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list.count(23))

print("")

age, height, name, surname = my_other_list
print(name)

print("")

print(my_list + my_other_list)

my_list = [45, 24, 23, 42]
print(my_list)
print(type(my_list))

print()

# Operaciones

my_other_list.append("NanoDev") # Inserta un nuevo elemento a la lista en la parte final
print(my_other_list)

my_other_list.insert(1, "Cian") # Inserta un nuevo elemento a la lista en la posicion que le digamos
print(my_other_list)

my_other_list[1] = "Rojo" # Modifica el elemento de la posicion dada entre [] y lo cambia por el nuevo objeto
print(my_other_list)

my_other_list.remove("Rojo") # Elimina el elemento que le digamos
print(my_other_list)

my_other_list.pop() # Elimina el ultimo elemento de la lista pero lo recuerda
print(my_other_list.pop())
print(my_other_list)

del my_other_list[2] # Borra el elemento de la posicion que le pasemos
print(my_other_list)

my_other_list.clear() # Elimina todos los elementos de la lista
print(my_other_list)

my_new_list = my_list.copy() # Copia todos los elementos de una lista a otra

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() # Ordena la lista del último elemento al primero
print(my_new_list)

my_new_list.sort() # Ordena los elementos de menor a mayor o alfabetico por defecto
print(my_new_list)