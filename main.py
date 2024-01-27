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

def lookpath(padre, objetivo, opciones = [], actual = []):
    padre = int(padre)
    objetivo = int(objetivo)

    if padre > objetivo:
        for pal in pals:
            nombre, numero = pal
            numero = int(numero)
            if numero < padre:
                if len(actual) == 0:
                    actual.append(numero)
                    numero = (numero + padre)/2
                    actual.append(numero)
                    posible = lookpath(numero, objetivo, opciones, actual)
                elif actual[len(actual)-2] != numero:
                    actual.append(numero)
                    numero = (numero + padre)/2
                    actual.append(numero)
                    posible = lookpath(numero, objetivo, opciones, actual)
                    
def searchpal():
    

    elif padre < objetivo:
        print("hola")

    else:
        if len(opciones) == 0:
            opciones.append(actual)
            return opciones
        elif len(opciones[0]) < len(actual):
            return opciones
        elif len(opciones[0]) == len(actual):
            opciones.append(actual)
            return opciones
        else:
            opciones.clear()
            opciones.append(actual)
            return opciones
            
            


with open('infopals.txt', 'r') as archivo:
        pals = [nombre.strip().lower().split(' - ') for nombre in archivo.readlines()]

objetivo = ""

print("¿objetivo?")
numero_objetivo = 280 #buscapal()

print("¿padre?")
padre = 660 #buscapal()

lista = lookpath(padre, numero_objetivo)

print(lista)