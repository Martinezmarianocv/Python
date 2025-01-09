#03 ESTRUCTURAS DE DATOS

'''
* EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

''' Listas '''
# Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas.
# Ambas maneras sirven para definir una lista

mi_lista = list()    
mi_otra_lista = []

mi_lista = ["Mariano", "Martinez", 24, "Python"]
print(mi_lista)

print(mi_lista[0]) # Para llamar a un elemento de la lista

mi_lista.append("NanoDev") # Inserta un nuevo elemento a la lista en la parte final
print(mi_lista)

mi_lista.insert(1, "Cian") # Inserta un nuevo elemento a la lista en la posicion que le digamos
print(mi_lista)

mi_lista[1] = "Rojo" # Modifica el elemento de la posicion dada entre [] y lo cambia por el nuevo objeto
print(mi_lista)

mi_lista.remove("Rojo") # Elimina el elemento que le digamos
print(mi_lista)

mi_lista.pop() # Elimina el ultimo elemento de la lista pero lo recuerda
print(mi_lista.pop())
print(mi_lista)

del mi_lista[2] # Borra el elemento de la posicion que le pasemos
print(mi_lista)

mi_otra_lista = mi_lista.copy() # Copia todos los elementos de una lista a otra
print(mi_otra_lista)

mi_lista.clear() # Elimina todos los elementos de la lista
print(mi_lista)

mi_otra_lista.reverse() # Ordena la lista del último elemento al primero
print(mi_otra_lista)

mi_otra_lista.sort() # Ordena los elementos de menor a mayor o alfabetico por defecto
print(mi_otra_lista)

print("") # Para dejar un espacio

''' Tuplas '''

# Una tupla es un conjunto de valores CONSTANTES, no se pueden cambiar los datos ya dados tal como con las variables o las listas

mi_tupla = ("Mariano", "Martinez", 24, "Python")
print(mi_tupla)

print(mi_tupla[0]) # Para llamar a un elemento de la lista

print(mi_tupla.count("Martinez")) # Cuenta la cantidad de elementos dados, en la tupla

print(mi_tupla.index("Martinez")) # Dice en que posicion esta el elemento dado

''' mi_tupla[1] = 1.73   no se pueden cambiar los valores ya dados
print(mi_tupla)          a las tuplas '''

print(mi_tupla[2:6]) # Esto me devuelve los valores que estan entre la posicion 2 y la 6 dentro de la tupla

# Para agregar elementos a una tupla debemos convertirlo en lista y posteriormente convertirlo en tupla:

mi_tupla = list(mi_tupla) # Cambiamos de tupla a lista
print(type(mi_tupla))

mi_tupla[3] = "NanoDev"
mi_tupla.insert(1, "Cian")
print(mi_tupla)

mi_tupla = tuple(mi_tupla) # Cambiamos de lista a tupla
print(type(mi_tupla))

''' del mi_tupla  Elimina la variable completa y no debemos hacerlo, es un ERROR
print(mi_tupla)   NameError: name 'mi_tupla' is not defined '''

print("") # Para dejar un espacio

''' Sets '''

# Un set tiene una lista de base y se utilzian con mas sentido cuando neceistamo valores que no se repitan

mi_set = set(["Martinez", "Mariano"])
mi_otro_set = {}

print(type(mi_set))
print(type(mi_otro_set)) # Por las llaves {} inicialmente es un diccionario vacio

mi_otro_set = {"Martinez", "Mariano", 23} # Vamos a entenderlo como una lista
print(type(mi_otro_set)) # Ahora que le asigamos valores entre las llaves pasa a ser un SET. Esto por la forma en la que agregamos los datos

print(len(mi_otro_set)) # Cuenta los elementos que hay dentro del set

# print(my_other_set[2]) TypeError: 'set' object is not subscriptable

mi_otro_set.add("NanoDev")  # Un set no es una estructura ordenada
print(mi_otro_set) # Los elementos no se guardan de forma ordenada como en las listas o tuplas, por lo que no podemos extraer un elemento de dento con Print(mi_otro_set[2])

# Tampoco deja repetir datos, es decir, no pueden haber dos datos iguales dentro de los sets

# Tambien es variable ya que que podemos agregar nuevos elementos.

print("Martinez" in mi_otro_set) # esto es para ver si x elemento pertenece a nuestro set
print("Marutinez" in mi_otro_set) # Devuelve valores bool

mi_otro_set.remove("Martinez") # Elimina el elemento que le pasamos
print(mi_otro_set)

mi_otro_set.clear()  # Borra todos los elementos de nuestro set
print(len(mi_otro_set)) 

''' del mi_otro_set Elimiamos la propiedad por completo
print(mi_otro_set) NameError: name 'mi_otro_set' is not defined '''

mi_set.add(24) # Agrega un solo elemento al set
print(mi_set)

mi_set.remove(24) # Elimina el elemento que se pasa como parámetro. Si no se encuentra, se lanza la excepción KeyError
print(mi_set)

mi_set.discard(24)# Borra el elemento que se pasa como parámetro, y si no se encuentra no hace nada
print(mi_set)

mi_set.pop() # El método pop() elimina un elemento aleatorio del set
print(mi_set)

mi_nuevo_set = {1, 2, 3}

print(mi_set.union(mi_nuevo_set)) # Esta operación representa la “mezcla” de ambos sets.

mi_nuevo_set = mi_set.union(mi_nuevo_set)
print(mi_nuevo_set)

print("") # Para dejar un espacio

''' Diccionarios '''

# Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value

mi_dict = dict()
mi_otro_dict = {}
print(type(mi_dict))
print(type(mi_otro_dict))

mi_otro_dict = {"Nombre":"Mariano", "Apellido":"Martinez", "Edad":23, 1:"Python"} # Definimos un diccionario en relacion clave = valor
print(mi_otro_dict)

mi_dict = {
    "Nombre":"Mariano", 
    "Apellido":"Martinez",
    "Edad":23, 
    "Lenguajes": {"Python", "HTML", "CSS"},
    3:1.70,
}
print(mi_dict)

print(len(mi_dict)) # Nos dice la cantidad de elementos definidos que tenemos

print(mi_dict["Nombre"]) # Damos la Clave para que nos devuelva el Valor

mi_dict["Nombre"] = "Sofia" # Cambiamos el valor de la clave
print(mi_dict["Nombre"])

mi_dict["Equipo"] = "Defensa y Justicia" # Agregamos una clave junto con su valor
print(mi_dict["Equipo"])
print(mi_dict)

del mi_dict["Equipo"] # Eliminamos la Clave que le pasamos entre [] y no se pueden recuperar
print(mi_dict)

print("Mariano" in mi_dict) # Da False porque busca por clave, no por valor
print("Nombre" in mi_dict) # Da True porque existe la clave

print(mi_dict.items()) # Devuelve los items del diccionario
print(mi_dict.keys())   # Devuelve solo las claves
print(mi_dict.values()) # Devuelve todos los valores

print("") # Para dejar un espacio

'''
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos. (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
'''


def agendaDeContactos():

    agenda = {}

    def agregarContacto():

        telefono = input("Ingresa el número de telefono: ")    
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
            agenda[nombre] = {telefono}
        else:
            print("El número de telefono debe ser de máximo 11 dígitos.")

    while True:

        print("")
        print("1: Buscar Contacto")
        print("2: Agregar Contacto")
        print("3: Actualizar Contacto")
        print("4: Eliminar Contacto")
        print("5: Salir de la Agenda")

        opcion = input("elige una opción: ")

        match opcion:

            case "1":
                nombre = input("Ingresa el nombre del contacto: ")
                if nombre in agenda:
                    print(f"El número de telefono de {nombre} es {agenda[nombre]}")
                else:
                    print(f"El contacto {nombre} no existe.")

            case "2":
                nombre = input("Ingrese nombre del contacto a agregar: ")
                agregarContacto()

            case "3":
                nombre = input("Ingrese el nombre del contacto a aztualizar: ")
                if nombre in agenda:
                    agregarContacto()
                else:
                    print(f"El contacto {nombre} no existe.")

            case "4":
                nombre = input("Ingrese el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                else:
                    print(f"El contacto {nombre} no existe.")

            case "5":
                print("Saliendo de la Agenda...")
                break

agendaDeContactos()
