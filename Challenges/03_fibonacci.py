#3 LA SUCESIÓN DE FIBONACCI

'''
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
*  La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
*  0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
    prev_number = 0
    netx_number = 1

    for index in range(50):
        print(prev_number)

        fib = prev_number + netx_number
        prev_number = netx_number
        netx_number = fib

fibonacci()
