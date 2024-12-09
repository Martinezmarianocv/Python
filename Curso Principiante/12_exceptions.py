# Excepciones

# Manejo de errores

number_one, number_two = 5, 1

number_two = "1"

# Try Except

try: 
    print(number_one + number_two)
    print("No se ah producido un error")
except:
    print("Se ha producido un error")

# Try except else

try: 
    print(number_one + number_two)
    print("No se ah producido un error")
except:
    print("Se ha producido un error")
else: # Si hay exceptción no se ejecuta el else. Se ejecuta solo cuando el try no da error y es opcional
    print("La ejecución continúa correctamente")

# Try except else finally

try: 
    print(number_one + number_two)
    print("No se ah producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally: # Se ejecuta siempre y es opcional
    print("La ejecución continúa")

# Captura de excepciones por tipo

try: 
    print(number_one + number_two)
    print("No se ah producido un error")
except TypeError: # Se ejecuta solo si se produce un TypeError
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try: 
    print(number_one + number_two)
    print("No se ah producido un error")
except ValueError as error: # Con el as .. creamos una variable, en este caso error, donde vamos a poder guardar la información sobre el error
    print(error)
except Exception as error:
    print(error)