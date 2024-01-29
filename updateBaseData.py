import csv
import json
from pal import Pal

"""
metodo para buscar un pal por el nombre
"""
def buscar_pal(nombre_pal):
        for pal in pals:
                if pal.nombre.lower() == nombre_pal.lower():
                        return pal

# Leer los resultados de la cría desde el archivo CSV
with open('BreedingsResults.csv', 'r') as f:
    data = f.read()
    resultados = data.replace('\n', ',').split(',')

with open('infopals.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')
    Npals = [line.split(' - ') for line in data]
# Crear los datos JSON

pals = []
for pal in Npals:
    pals.append(Pal(pal[0], pal[1]))

del Npals
del data
del f
del pal
datos = []
i = 0
for padre1 in pals:
    for padre2 in pals:
        resultado = buscar_pal(resultados[i])
        datos.append({
            "padre1": padre1.to_dict(),
            "padre2": padre2.to_dict(),
            "resultado": buscar_pal(resultados[i]).to_dict()  # Asume que los resultados están en el mismo orden
        })
        i += 1

# Escribir los datos en un archivo JSON
with open('breeding.json', 'w') as f:
    json.dump({"datos": datos}, f, indent=4)