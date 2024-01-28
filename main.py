import json

pals = []
with open('infopals.txt', 'r') as archivo:
        Npals = [nombre.strip().lower().split(' - ') for nombre in archivo.readlines()]
        for nombre, poder in Npals:
            pals.append(Pal(nombre, poder, []))
        del Npals

datos = []

for pal in pals:
    for pal2 in pals:
        print(pal.nombre, pal2.nombre)
        print("hijo?")
        hijo = input()
        dato = {
        "padre1": pal,
        "padre2": pal2,
        "resultado": hijo
        }
        datos.append(dato)

json_data = {
    "datos": datos
}

json_string = json.dumps(json_data, indent=4)
print(json_string)

