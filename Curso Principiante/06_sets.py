# Un set tiene una lista de base y se utilzian con mas sentido cuando neceistamo valores que no se repitan

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Por las llaver {} inicialmente es un diccionario vacio

my_other_set = {"Martinez", "Mariano", 23} # Vamos a entenderlo como una lista
print(type(my_other_set)) # Ahora que le asigamos valores entre las llaves pasa a ser un SET. Esto por la forma en la que agregamos los datos

print(len(my_other_set))

# print(my_other_set[2]) TypeError: 'set' object is not subscriptable

my_other_set.add("NanoDev")  # Un set no es una estructura ordenada
print(my_other_set) # Los elementos no se guardan de forma ordenada como en las listas o tuplas, por lo que no podemos extraer un elemento de dento con Print(my_other_list[2])

# Tampoco deja repetir datos, es decir, no pueden haber dos datos iguales dentro de los sets

# Tambien es variable ya que que podemos agregar nuevos elementos.

print("Martinez" in my_other_set) # esto es para ver si x elemento pertenece a nuestro set
print("Marutinez" in my_other_set) # Devuelve valores bool

my_other_set.remove("Martinez") # Elimina el elemento que le pasamos
print(my_other_set)

my_other_set.clear()  # Borra todos los elementos de nuestro set
print(len(my_other_set)) 

''' del my_other_set Elimiamos la propiedad por completo
print(my_other_set) NameError: name 'my_other_set' is not defined '''

my_set = {"Martinez", "Mariano", 23}
my_list = list(my_set)

print(my_list)
print(my_list[2])

my_other_set = {"python", "HTML", "CSS"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set)) # Queda igual que antes ya que no se pueden repetir los elementos

print(my_new_set.union({"JavaScript", "TypeScript"})) # Ahroa si se agregan estos elementos ya que no son repetidos

print(my_new_set.difference(my_set)) # Quitamos los elementos de my_set que figuran dentro de my_new_set


