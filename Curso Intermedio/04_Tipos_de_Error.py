# Tipos de Error

# SyntaxError

''' print"Hola Mundo" = Error | Faltan parentesís '''

# NameError

''' print(name) = NameError | name no esta definido '''

# IndexError

''' 
my_list = ["Python", "Java", "HTML"]
print(my_list[5]) = IndexError | No hay elemento 5 en la lista
'''

# ModuleNotFoundError

''' import maths = ModuleNotFoundError | El modulo no se encuentra ya que no existe '''

# AtributeError

''' print(math.PI) = AtributeError | No existe PI sino pi '''

# KeyError

''' 
my_dict = {"nombre":"Mariano", "Edad":35, 1:"Python"}
print(my_dict["nombe"]) | La clave "nombre" esta mal escrita
'''

# TypeError

''' 
my_list = ["Nombre"] 
print(my_list["Nombre"]) | No podemos llamar a elementos de una lista con un str, necesitamos un int
'''

# ImportError

''' 
from math import PI | No se puede importar el PI de math ya que este PI no existe
'''

# ValueError

'''
my_int = int("10 años") | No se puede tranformar una cadena de texto a entero. Solo se puede transfromar el 10
print(my_int)
'''

# ZeroDivisionError

'''
print(4/0) | No se puede dividir por 0
'''