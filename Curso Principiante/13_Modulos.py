# Modulos

# Un módulo es una libreria o lugar donde tenemos codigo que inicialmente no esta en nuestro programa. Todos nuestros ficheros son módulos y podemos acceder a ellos.

import module # Importamos el modulo
# from module import sum ... Para importar solo la función

module.sum(5, 3, 1)  # Llamamos a la funcion del modulo
module.printValue("Hola Python")

# from module import sum ... Para importar solo la función
# sum(5, 3, 1) ... Para llamar utilizar la función 

import math  # También hay muchos modulos de Python

print(math.pi)
print(math.pow(2, 8))

