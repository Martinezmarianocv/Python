# Su estructura ayuda a relacionar datos

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Mariano", "Apellido":"Martinez", "Edad":23, 1:"Python"} # Definimos un diccionario en relacion clave = valor
print(my_other_dict)

my_dict = {
    "Nombre":"Mariano", 
    "Apellido":"Martinez",
    "Edad":23, 
    "Lenguajes": {"Python", "HTML", "CSS"},
    3:1.70,
}

print(my_dict)

print(len(my_dict)) # Nos dice la cantidad de elementos definidos que tenemos

print(my_dict["Nombre"]) # Damos la Clave para que nos devuelva el Valor

my_dict["Nombre"] = "Sofia" # Cambiamos el valor de la clave
print(my_dict["Nombre"])

my_dict["Equipo"] = "Defensa y Justicia" # Agregamos una clave junto con su valor
print(my_dict["Equipo"])
print(my_dict)

del my_dict["Equipo"] # Eliminamos la Clave que le pasamos entre [] y no se pueden recuperar
print(my_dict)

print("Mariano" in my_dict) # Da False porque busca por clave, no por valor
print("Nombre" in my_dict) # Da True porque existe la clave

print(my_dict.items()) # Devuelve los items del diccionario
print(my_dict.keys())   # Devuelve solo las claves
print(my_dict.values()) # Devuelve todos los valores

my_new_dict = my_other_dict.fromkeys(("Nombre", 3, "Equipo")) # Creamos un diccionario nuevo sin valores. No nos sirve para nada

print(my_new_dict)


# Importar todo un diccionario

my_new_dict = dict.fromkeys(my_dict) # Esto si ya tiene mas sentidos para
print(my_new_dict)                   # Su uso

my_new_dict = dict.fromkeys(my_dict, ("Mariano", "Martinez")) # Le damos estos valores a todas las claves
print(my_new_dict)

print()

my_new_dict = dict.fromkeys(my_dict, my_dict) # Le damos a cada clave todas las claves y valores de los diccionarios
print(my_new_dict)

print()

my_new_dict = dict.fromkeys(my_dict, "Mariano") # Lo que pasa con esto es que solo podemos repetir el valor dado dentro de todas las claves. No se puede dar un valor diferente para cada clave
print(my_new_dict)