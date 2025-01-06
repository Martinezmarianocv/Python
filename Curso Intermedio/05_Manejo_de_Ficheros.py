# Manejo de Ficheros

# .txt file

import os

txt_file = open("Curso Intermedio/my_file.txt", "r+") # Modo para leer y escribir
#print(txt_file.read()) # Lee todo el fichero
print(txt_file.read(10)) # Lee solo los primeros 10 caracteres
print(txt_file.readline()) # Lee línea a línea del fichero
print(txt_file.readlines()) # Lee varias líneas como si fuera un for

txt_file.write("\nAunque también me gusta Java") # Escribe en el fichero | el \n es para escribir en una nueva línea

# os.remove("Curso Intermedio/my_file.txt") para borrar el fichero

txt_file.close()

print("")

# .json file 

import json

json_file = open("Curso Intermedio/my_file.json", "w+")          

json_test = {
    "name": "Mariano",
    "surname": "Martinez",
    "age": 24,
    "languages": ["Python", "JavaScript", "HTML"],
    "website": "nano.dev"
}

json.dump(json_test, fp=json_file, indent=4)

json_file.close()

json_dict = json.load(open("Curso Intermedio/my_file.json"))
print(json_dict) # Hacemos que el fichero json se vuelva diccionario

print(type(json_dict))

print(json_dict["name"])

print("")

# .csv file

import csv

csv_file = open("Curso Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "langauge", "website"])
csv_writer.writerow(["Mariano", "Martinez", "24", "Python", "nano.dev"])
csv_writer.writerow(["Facundo", "Martinez", "17", "HTML", "facu.dev"])

csv_file.close()

with open("Curso Intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
'''import xlrd | debe instalarse el modulo'''

# xml file

import xml