import json
from pal import Pal

pals = []
with open('infopals.txt', 'r') as archivo:
        Npals = [nombre.strip().lower().split(' - ') for nombre in archivo.readlines()]
        for nombre, poder in Npals:
            pals.append(Pal(nombre, poder))
        del Npals


resultados = []
with open('resultados.csv', 'r') as archivo:
    for linea in archivo.readlines():
        resultados.extend(linea.strip().split(',')[1:])

datos = []

i = 0
for pal in pals:
    for pal2 in pals:
        print(pal.nombre, pal2.nombre)
        dato = {
        "padre1": pal.to_dict(),
        "padre2": pal2.to_dict(),
        "resultado": resultados[i]
        }
        datos.append(dato)
        i += 1

json_data = {
    "datos": datos
}

with open('breeding.json', 'w') as archivo:
    json.dump(json_data, archivo, indent=4)