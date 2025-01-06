# Manejo de Paquetes 

# Como usar cualquier modulo que no tengamos descargados

''' PIP https://pypi.org '''

# pip install pip
# pip --version

import numpy

import mypackage.arithmetics # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 17])

print(type(numpy_array))

print(numpy_array * 2)

import pandas # pip install pandas

# pip list | listado de paquetes instalados
# pip uninstall pandas | Eliminar paquete
# pip show numpy | Muestra información sobre el paquete

import requests # Para hacer peticiones a una api

response = requests.get("https://pokeapi.co/api/v2/pokemon?limiy=151")

print(response)
print(response.status_code)
print(response.json())

print("")

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))