# Funciones de Orden Superior

from functools import reduce

# Son funciones que hacen cosas con funciones dentro.

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, sum_f):
    return sum_f(first_value + second_value)

print(sum_two_values_and_one(5, 2, sum_one))
print(sum_two_values_and_one(5, 2, sum_five))

# Closures

# Función que define una finción y retorna una función

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(5)
print(add_closure(5))

# Built-in Higher Order Functions

numbers = [2, 5, 10, 21, 3, 30]

# Map: Necesita una lista de valores

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter: Filtra los valores de la lista

def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce: Opera con un valor más es acumulado, es decir, suma todos los valores de a dos y le suma un nuevo valor del listado.

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))