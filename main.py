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

def lookpath(padre, objetivo, limit, opciones = [], actual = []):
    if limit <= len(actual):
        actual.clear()
        return opciones
    padre = int(padre)
    objetivo = int(objetivo)

    if len(actual) != 0:
        if actual[len(actual)-1] == objetivo:
            opciones.append(actual)
            return opciones

    numero = posiblepal(objetivo, padre)

    if numero < padre:
        if len(actual) == 0:
            actual.append(numero)
            numero = searchpal((numero + padre)/2)
            actual.append(numero)
            posible = lookpath(numero, objetivo, limit, opciones, actual)
        elif actual[len(actual)-2] != numero:
            actual.append(numero)
            numero = searchpal((numero + padre)/2)
            actual.append(numero)
            posible = lookpath(numero, objetivo, limit, opciones, actual)

    if numero > padre:
        if len(actual) == 0:
            actual.append(numero)
            numero = searchpal((numero + padre)/2)
            actual.append(numero)
            posible = lookpath(numero, objetivo, limit, opciones, actual)
        elif actual[len(actual)-2] != numero:
            actual.append(numero)
            numero = searchpal((numero + padre)/2)
            actual.append(numero)
            posible = lookpath(numero, objetivo, limit, opciones, actual)

    """
    if padre > objetivo:
        for pal in pals:
            nombre, numero = pal
            numero = int(numero)
            if numero < padre:
                if len(actual) == 0:
                    actual.append(numero)
                    numero = searchpal((numero + padre)/2)
                    actual.append(numero)
                    posible = lookpath(numero, objetivo, limit, opciones, actual)
                elif actual[len(actual)-2] != numero:
                    actual.append(numero)
                    numero = searchpal((numero + padre)/2)
                    actual.append(numero)
                    posible = lookpath(numero, objetivo, limit, opciones, actual)
                    

    elif padre < objetivo:
         for pal in pals:
            nombre, numero = pal
            numero = int(numero)
            if numero > padre:
                if len(actual) == 0:
                    actual.append(numero)
                    numero = searchpal((numero + padre)/2)
                    actual.append(numero)
                    posible = lookpath(numero, objetivo, limit, opciones, actual)
                elif actual[len(actual)-2] != numero:
                    actual.append(numero)
                    numero = searchpal((numero + padre)/2)
                    actual.append(numero)
                    posible = lookpath(numero, objetivo, limit, opciones, actual)
                    """

    
            
            
def searchpal(numero):
    numero = int(numero)
    powers = [int(power) for nombre, power in pals if int(power) != numero]
    powers_greater_equal = [power for power in powers if power >= numero]
    if powers_greater_equal:
        closest = min(powers_greater_equal, key=lambda x: abs(x - numero))
    else:
        closest = max(powers, key=lambda x: abs(x - numero))
    return closest

def posiblepal(objetivo, padre):
    numero = (objetivo + padre)/2
    numero = int(numero)
    powers = [int(power) for nombre, power in pals if int(power) != objetivo]
    powers_greater_equal = [power for power in powers if power >= numero]
    if powers_greater_equal:
        closest = min(powers_greater_equal, key=lambda x: abs(x - numero))
    else:
        closest = max(powers, key=lambda x: abs(x - numero))
    return closest

with open('infopals.txt', 'r') as archivo:
        pals = [nombre.strip().lower().split(' - ') for nombre in archivo.readlines()]


print("¿objetivo?")
numero_objetivo = 190 #buscapal()

print("¿padre?")
padre = 150 #buscapal()

if padre > numero_objetivo:
    pals = sorted(pals, key=lambda x: int(x[1]))
else:
    pals = sorted(pals, key=lambda x: int(x[1]), reverse=True)

lista = lookpath(padre, numero_objetivo, 5, [], [])

print(lista)