# List Comprehension

# Es una forma de crear listas de manera rápida o a partir de listas ya creadas

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(7)] # Se imprimen los primeros 7 valores
print(my_list)

my_range = range(7)
print(list(my_range))

my_list = [i + 1 for i in range(7)]
print(my_list)

my_list = [i * 2 for i in range(7)]
print(my_list)

my_list = [i * i for i in range(7)] # Multiplicamos cada objeto de la lista por si mismo
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(7)]
print(my_list)