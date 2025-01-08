# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

## Ejercicio

'''
* - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
* - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
* - Crea una variable (y una constante si el lenguaje lo soporta).
* - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
'''

# https://www.python.org/

# Este es un comentario en una sola línea

'''
este es
un comentario
en varias 
líneas
'''

"""
Este también es
un comentario
en varias líneas
"""

mi_variable = "Esta es mi variable"
mi_variable = "Este es el nuevo valor de mi variable"

MI_CONSTANTE = "Esta es mi constante"

mi_string = "Este es mi string"
mi_int = 5
mi_bool = True
mi_float = 1.4

print(type(mi_int))
print(type(mi_float))
print(type(mi_bool))
print(type(mi_string))

print("Hola Python")