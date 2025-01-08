#01 OPERADORES Y ESTRUCTURAS DE CONTROL

'''
* EJERCICIO:
* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
        (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
    Condicionales, iterativas, excepciones...
* - Debes hacer print por consola del resultado de todos los ejemplos.
'''

''' Operadores aritméticos '''

num1 = 4 
num2 = 2

print(num1 + num2) # SUMA
print(num1 - num2) # RESTA
print(num1 * num2) # MULTIPLICACIÓN
print(num1 / num2) # DIVISIÓN
print(num1 % num2) #  MÓDULO
print(num1 ** num2) # EXPONENTE
print(num1 // num2) # COCIENTE

print("") # Para crear un espacio

''' Operadores de comparación '''

num1 = 4 
num2 = 2

print(num1 == num2) # IGUAL A
print(num1 != num2) # DISTINTO DE
print(num1 > num2) # MAYOR QUE
print(num1 < num2) # MENOR QUE
print(num1 >= num2) # MAYOR IGUAL QUE
print(num1 <= num2) # MENOR IGUAL QUE

print("") # Para crear un espacio

''' Operadores lógicos '''

verdadero = True
falso = False

# El operador AND devuelve TRUE si ambos son TRUE
print(verdadero and falso) 
print(verdadero and verdadero) 
print(falso and falso)

print("") # Para crear un espacio

# El operador OR devuelve TRUE si al menos uno de los dos es TRUE
print(verdadero or falso)
print(falso or falso)
print(verdadero or verdadero)

print("") # Para crear un espacio

# EL operador OR devuelve el valor contrario del elemento, si es TRUE devuelve FALSE
print(not verdadero)
print(not falso)

print("") # Para crear un espacio

''' Operadores de bit a bit '''

num_binario = bin(27)
print(num_binario)

bin1 = 0b1101
bin2 = 0b1011

print("") # Para crear un espacio

# El operador & recorre ambos números en su representación binaria elemento a elemento, y hace una operación and con cada uno de ellos, delvolviendo 1 si ambos son 1 y 0 si uno de ellos es 0.

print(bin(bin1 & bin2))
# 0b1001

print("") # Para crear un espacio

# El operador | realiza la operación or elemento a elemento con cada uno de los bits de los números que introducimos, devolviendo 1 cuando haya al menos un 1.

print(bin(bin1 | bin2))
# 0b1111

print("") # Para crear un espacio

# El operador ~ realiza la operación not sobre cada bit del número que le introducimos, es decir, invierte el valor de cada bit, poniendo los 0 a 1 y los 1 a 0. 
# El comportamiento en Python puede ser algo distinto del esperado. En el siguiente ejemplo, tenemos el número 40 que en binario es 101000. Si hacemos ~101000 sería de esperar que como hemos dicho, se inviertan todos los bits y el resultado sea 010111, pero en realidad el resultado es 101001.
# Si vemos el resultado con números decimales, es equivalente a hacer ~a sería -a-1 como se puede ver en el siguiente ejemplo. En este caso, en vez de mostrar el valor binario mostramos el decimal, y se puede ver como efectivamente si a=40, tras aplicar el operador ~ el resultado es -40-1.

print(bin(~bin1))
# -0b1110

print("") # Para crear un espacio

# El operador realiza la función xor con cada bit de las dos variables que se le proporciona. Realiza la función xor con cada bit de las dos variables que se le proporciona.

x = 0b0110 ^ 0b1010
print(bin(x))
# 0 xor 1 = 1
# 1 xor 0 = 1
# 1 xor 1 = 0
# 0 xor 0 = 0
# 0b1100

print("") # Para crear un espacio

# El operador >> desplaza todos los bit x unidades a la derecha. Por lo tanto es necesario proporcionar dos parámetros, donde el primer es el número que se desplazará o shift y el segundo es el número de posiciones. Es importante notar que Python por defecto elimina los ceros a la izquierda, ya que igual que en el sistema decimal, son irrelevantes.

print(bin(bin1 >> 2))
# bin1 = 0b1101
# 0b11

print("") # Para crear un espacio

# El operador << es análogo al >> con la diferencia que en este caso el desplazamiento es realizado a la izquierda. Queremos destacar que aunque la entrada sean 4 bits, Python internamente rellena todo lo que está a la derecha con ceros como también si el número binario empieza con 1 solo agregara 0 a la derecha.

print(bin(bin1 << 2))
# bin1 = 0b1101
# 0b110100

print("") # Para crear un espacio

''' Operadores de asignacion '''

# Los operadores de asignación nos permiten realizar una operación y almacenar su resultado en la variable inicial. Podemos ver como realmente el único operador nuevo es el =.

mi_num = 11 # ASIGNACIÓN
print(mi_num)

mi_num += 1 # SUMA Y ASIGNACIÓN
print(mi_num)

mi_num -= 1 # RESTA Y ASIGNACIÓN
print(mi_num)

mi_num *= 2 # MULTIPLICACIÓN Y ASIGNACIÓN
print(mi_num)

mi_num /= 2 # DIVISIÓN Y ASIGNACIÓN
print(mi_num)

mi_num **= 2 # EXPONENTE Y ASIGNACIÓN
print(mi_num)

mi_num //= 2 # DIVISIÓN ENTERA Y ASIGNACIÓN
print(mi_num)

mi_num %= 2 # MÓDULO Y ASIGNACIÓN
print(mi_num)

print("") # Para crear un espacio

''' Operadores de pertenencia '''

# Los operadores de pertenencia en Python son "in" y "not in" y se utilizan para verificar si un valor o variable está presente en una secuencia. 

mi_lista = [1, 2, 3, 4, 5, 6]

# IN evuelve True si el pertenece a la secuencia

print(4 in mi_lista)
print(7 in mi_lista)

# Not IN devuelve False si el elemento no pertenece a la secuencia
print(7 not in mi_lista)
print(4 not in mi_lista)

print("") # Para crear un espacio

''' Operadores de identidad '''

# El operador de identidad o identity operator is nos indica si dos variables hacen referencia al mismo objeto. Esto implica que si dos variables distintas tienen el mismo id(), el resultado de aplicar el operador is sobre ellas será True.

# El operador IS comprueba si dos variables hacen referencia a el mismo objeto. 

num1 = 4
num2 = 4

print(num1 is num2) 

# El operador IS NOT Devuelve True cuando ambas variables no hacen referencia al mismo objeto.

num1 = 4
num2 = 7

print(num1 is not num2)

print("") # Para crear un espacio

''' Estructuras de control '''

''' Condicionales '''

# Representan la manera de establecer flujos de ejecución de nuestro código

# Si se cumple una condición yo ejecuto lo que tu me digas que esta dentro del condicional

a = 10
b = 30

if a > b:
    print("a es mayor que b") # Primera condición
elif a < b:
    print("a es menor que b") # Segunda condición
else:
    print("a es igual a b") # Condición por default

print("") # Para crear un espacio

''' Loops / Bucles / Ciclos'''

# Sirve para iterar (Repetir el mismo códogo varias veces)

# While : Debemos pasarle una condición, mientras que haya una expresión es verdadero

mi_condición = 0

while mi_condición < 10: # Se ejecuta hasta que mi_condición sea el numero más cercano a 10
    print(mi_condición)
    mi_condición += 2
    if mi_condición == 10: 
        print("Mi condición es igual que 10")

print("") # Para crear un espacio

# For : Debe cumplir una condición e itera un grupo de elementos. Hace que un codigo se repita tantas veces como elementos tengamos iterables. Cada vez que repite el codigo tiene acceso al elemento siguiente de la lista/set/tupla/diccionario.

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print("") # Para crear un espacio

''' Manejo de Excepciones '''

'''
try:
    # Código que puede generar una excepción
    # Si ocurre una excepción aquí, el control se transfiere al bloque except
except ExcepciónX:
    # Código que maneja la excepción de tipo ExcepciónX
'''

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

try:
    c = a / b 
except ZeroDivisionError:
    print("Estás intentando dividir por cero")
finally:
    print("Ha finalizado el manejo de excepciones")

print("") # Para crear un espacio

'''
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

def programa():
    for index in range(10, 56):
        if index != 16 and index % 3 != 0 and index % 2 == 0:
            print(index)

programa()