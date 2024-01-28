with open('infopals.txt', 'r') as archivo:
        pals = [nombre.strip().lower().split(' - ') for nombre in archivo.readlines()]


print("¿objetivo?")
numero_objetivo = 190

print("¿padre?")
padre = 150

lista = lookpath(padre, numero_objetivo, 5, [], [])

print(lista)