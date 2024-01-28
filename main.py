import json

with open("infopals.txt", "r") as file:
    for pal in 

datos = []

for i in range(1, 4):
    dato = {
        "padre1": f"Padre1 del dato {i}",
        "padre2": f"Padre2 del dato {i}",
        "resultado": f"Resultado del dato {i}"
    }
    datos.append(dato)

json_data = {
    "datos": datos
}

json_string = json.dumps(json_data, indent=4)
print(json_string)