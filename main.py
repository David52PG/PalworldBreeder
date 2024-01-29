import json
import sys
from pal import Pal

"""
Apertura de bases de datos
"""
pals = []
with open("infopals.txt") as archivo:
        for linea in archivo:
                nombre, numero = linea.strip().split(" - ")
                pals.append([nombre, int(numero)])

# Leer el archivo JSON
with open("breeding.json") as file:
        data = json.load(file)

del linea, nombre, numero, archivo, file

"""
Metodo para solicitar un pal
"""
def pedir_pal():
        buscado = input()
        pal = buscar_pal(buscado)
        if pal == None:
                print("No se encontro el pal")
                return pedir_pal()
        else:
                return pal

"""
metodo para buscar un pal por el nombre
"""
def buscar_pal(nombre_pal):
        for pal in pals:
                if pal[0].lower() == nombre_pal.lower():
                        return pal

"""
buscar un pal por resultado de un apareamiento
"""
def buscar_resultado(nombre_resultado):
        resultados = []
        for resultado in data["datos"]:
                if resultado["resultado"]["nombre"].lower() == nombre_resultado.lower():
                        resultados.append(resultado)
        return resultados

"""
buscar el resultado de un apareamiento
"""
def buscar_apareamiento(padre1, padre2):
        for resultado in data["datos"]:
                if resultado["padre1"]["nombre"].lower() == padre1[0].lower() and resultado["padre2"]["nombre"].lower() == padre2[0].lower():
                        return buscar_pal(resultado["resultado"]["nombre"])
        return apareamientos

"""
metodo principal de busqueda
"""
soluciones = []
def lookpath(inicial, objetivo, Padre, limite, path=[]):
        # Verificar si hemos alcanzado el límite de búsqueda
        if limite == 0:
                return path

        padres = buscar_resultado(Padre[0])
        # Recorrer los paths padres de la criatura inicial
        for pareja in padres:
                if pareja['padre1'] == pareja['padre2']:
                                return
                path.append(buscar_pal(pareja['padre1']['nombre']))
                path.append(buscar_pal(pareja['padre2']['nombre']))
                for key in pareja:
                        if key == 'resultado':
                                continue
                        nombre_pal = pareja[key]['nombre']
                        Padre = buscar_pal(nombre_pal)
                        if Padre == inicial:
                                soluciones.append(path.copy())  # Copiar el contenido de path
                        else:
                                lookpath(inicial, objetivo, Padre, limite-1, path)
                path.pop()
                path.pop()
        return


limite = 1
print("¿de quien quieres partir?")
inicio = pedir_pal()
print("¿a quien quieres llegar?")
objetivo = pedir_pal()
path = [objetivo]

while len(soluciones) == 0:
        lookpath(inicio, objetivo, objetivo, limite, path)
        limite += 1
# Obtener la longitud mínima del array de soluciones
sorted_soluciones = sorted(soluciones, key=len)

del inicio, objetivo, path, soluciones, limite

# Imprimir las soluciones ordenadas por menor longitud
import graphviz


for sol in sorted_soluciones:
        dot = graphviz.Digraph(comment='Genealogical Tree')
        i = len(sol) - 1
        while i != 0:
                padre1 = sol[i]
                padre2 = sol[i - 1]
                hijo = buscar_apareamiento(padre1, padre2)
                dot.node(padre1[0], label=padre1[0])
                dot.node(padre2[0], label=padre2[0])
                dot.node(hijo[0], label=hijo[0])
                dot.edge(padre1[0], hijo[0])
                dot.edge(padre2[0], hijo[0])
                i = i - 2

        dot.render('genealogical_tree', format='png', view=True)
        input("Presiona Enter para continuar o introduce 'q' para detenerse: ")

        if input().lower() == 'q':
            sys.exit()