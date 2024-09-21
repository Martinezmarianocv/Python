my_string = "Mi String"
my_other_string = "Mi Otro String"

print(len(my_string) + len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \n con salto de línea"
print(my_new_line_string)

my_tab_string = "\t Este es un string con tabulación"
print(my_tab_string)

my_scape_string = "\t Este es un string \n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Mariano", "Martinez", 23

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) 
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # %s para los strings y %d para los enteros, esta es mejor para formateos
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Esta es mejor en general

# Desempaquetado de caracteres

language = "python"   #Debemos crear más variables para poder desempaquetar el total de letras de la variable languange, entonces a, b, c, d, e, f
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[2:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

language_slice = language[0:6:2] # Toma todos los string del 0 al 6 y luego da saltos cada dos caracteres, mostrando el 0, 2 y 4
print(language_slice)

print("")

# Reverse

reversed_language = language[::-1] # Da vuelta el valor del string
print(reversed_language)

print("")

# Funciones

print(language.capitalize()) # Pone el primer string con mayúscula
print(language.upper()) # Escribe todo el string en mayusculas
print(language.count("t")) # Cuenta cuantas veces aparece el valor dado en nuestra variable
print(language.isnumeric()) # Devuelve False si no es un número
print("5".isnumeric()) # Devuelve True si es un número
print(language.lower()) # Escribe todo el string con minusculas
print(language.upper().isupper()) # upper lo hace con una mayuscula e isupper devuelve true porque si esta en mayusculas
print(language.startswith("py")) # Devuelve True si el valor que damos es con el que comienza el valor de la variable

