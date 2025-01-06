# Expresiones Regulares

# Es un mecanismo que nos sirve para inspeccionar si una cadena de texto tiene ciertos elementos dentro

# Siempre empieza a buscar desde el principio por lo que si desde la primer palabra no encuentra lo buscado nos debolvera "done"

import re

my_string = "Esta es la lección número 7: Lección Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de Ficheros"

match = re.match("Esta es la lección", my_string, re.I) # El re.I ignora las mayúsculas y minúsculas
print(match)
start, end = match.span()
print(match.span())
print(my_string[start:end])

print("")

match = re.match("Esta no es la lección", my_other_string)
if match is not None: # Para comprobar el None
    print(match)
    start, end = match.span()
    print(match.span())
    print(my_other_string[start:end])

# Search

''' Encuenta las palabras en cualquier posición que se encuentren. Aunque este repetido solo lo encuentra una vez '''

search = re.search("lección", my_string, re.I)
print(search) 
start, end = search.span()
print(search.span())
print(my_string[start:end])

#findall

''' Arma un listado de la palabra o palabras que buscamos. Si la palabra se repite, también la repite en el listado '''

findall = re.findall("lección", my_string, re.I)
print(findall)

#split

''' Busca el patron que le mostremos y divide el texto a partir del mismo '''

print(re.split(":", my_string))

#sub

''' Es para sustituir una cadena de texto por otra '''

print(re.sub("lección|Lección", "LECCIÓN", my_string)) # Con | indicamos que cambie ambas palabras
print(re.sub("Expresiones Regulares", "RegEx", my_string))

print("")

# Patrones de Expresiones Regulares Personalizados

pattern = r"[l|L]ección" # Creamos nuestro patrón

print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

print("")

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

print("")

pattern = r"[a-z]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

print("")

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

print("")

# Para aprender y validar expreciones regulares

''' https://regex101.com '''