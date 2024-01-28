import json

with open('breeding.json', 'w') as archivo:
    data = json.load(archivo)
    print(data)