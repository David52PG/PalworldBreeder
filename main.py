import json
from pal import Pal


def buscar_pal(nombre):
    for pal in pals:
        if pal.nombre.lower() == nombre.lower():
            return pal
    return None


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
        hijo = buscar_pal(resultados[i])
        print(pal.nombre, pal2.nombre)
        dato = {
        "padre1": pal.to_dict(),
        "padre2": pal2.to_dict(),
        "resultado": hijo.to_dict()
        }
        datos.append(dato)
        i += 1

json_data = {
    "datos": datos
}

with open('breeding.json', 'w') as archivo:
    json.dump(json_data, archivo, indent=4)