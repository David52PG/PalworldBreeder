with open('infopals.txt', 'r') as archivo:
        nombres = [nombre.strip() for nombre in archivo.readlines()]

print("¿objetivo?")
objetivo = input()

numero = 0
for nombre in nombres:
    print(numero)
    numero += 1
    if objetivo == nombre:
        print("Encontrado: " + nombre)
        break