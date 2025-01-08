#02 FUNCIONES Y ALCANCE

'''
* EJERCICIO:
* - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
* - Comprueba si puedes crear funciones dentro de funciones.
* - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
* - Pon a prueba el concepto de variable LOCAL y GLOBAL.
* - Debes hacer print por consola del resultado de todos los ejemplos. (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
'''

''' Funciones '''

# Se utilizan para resolver 2 problemas, primero encapsular una logica muy concreta, es decir, resolver un problema concreto; en segundo, evitar errores ya que siempre que querramos resolver un prblema llamaremos a la funcion que lo resuelve evitando duplicar código

''' función sin parámetros o retorno de valores '''

def saludo():
    print("¡Hola!")
saludo()

print("") # Para dejar un espacio

''' función con un parámetro '''

def saludoMasNombre(nombre):
    print("¡Hola " + nombre + "!")
saludoMasNombre("Mariano")

print("") # Para dejar un espacio

''' función con múltiples parámetros con una sentencia de retorno '''

def suma(num1, num2):
    return num1 + num2
resultado = suma(4, 5) # Asignamos la función a una variable para luego imprimir el resultado
print(resultado)

print("") # Para dejar un espacio

''' Función dentro de función '''

def definirNombre():
    def name():
        nombre = str(input("Ingresa un Nombre: "))
        print("Mi nombre es " + nombre)
    name()
definirNombre()

print("") # Para dejar un espacio

''' Funciones del lenguaje '''

print(len("Mariano"))
print(type(1.2))
print("martinez".upper())

print("") # Para dejar un espacio

''' Variables Locales y Globales '''

# Las variables Locales son aquellas a las que solo se puede acceder desde dentro de la función
# Las variables globales son aquellas a las que se puede acceder desde cualquier parte del programa, incluso desde dentro de las funciones

variable_global = "mundo"

def holaMundo():
    variable_local = "Hola"
    print(f"{variable_local} {variable_global}!")
holaMundo()

def holaMundo2():
    global variable_global2 # Definimos que la variable es global para utilizarla fuera de la función
    variable_global2 = "Hola"
holaMundo2()
print(f"{variable_global2} {variable_global}!")

print("") # Para dejar un espacio

'''
* DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*
* Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
* Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
'''

def funcion(text1, text2)-> int :
    count = 0
    for index in range(1, 101):
        if index % 3 == 0:
            print(text1)
        elif index % 5 == 0:
            print(text2)
        elif index % 3 == 0 and index % 5 == 0:
            print(text1 + " y " + text2)
        
        else:
            print(index)
            count += 1
    return count
print(funcion("Soy multiplo de 3", "soy multiplo de 5"))