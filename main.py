def buscapal():
    encontrado = False
    objetivo = input().lower()
    for pal in pals:
        nombre, numero = pal
        if nombre == objetivo:
            encontrado = True
            return numero
    if encontrado!=True:
        print("No encontrado")
        buscapal()

with open('infopals.txt', 'r') as archivo:
        pals = [nombre.strip().lower().split(' - ') for nombre in archivo.readlines()]

objetivo = ""

print("¿objetivo?")
numero_objetivo = buscapal()

print("¿padre?")
padre = buscapal()

print(numero_objetivo)
print(padre)