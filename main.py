import json
import sys
from pal import Pal
import graphviz
import os

"""
Apertura de bases de datos
"""
# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Open the file using the absolute path
with open(os.path.join(script_dir, "infopals.txt")) as archivo:
    pals = []
    for linea in archivo:
        nombre, numero = linea.strip().split(" - ")
        pals.append([nombre, int(numero)])

# Do the same for the JSON file
with open(os.path.join(script_dir, "breeding.json")) as file:
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
        return None

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
def lookpath(inicial, objetivo, Padre, limite, path=[]):
        padres = buscar_resultado(Padre[0])
        # Recorrer los paths padres de la criatura inicial
        for pareja in padres:
                if pareja['padre1'] == pareja['padre2']:
                                continue
                path.append(buscar_pal(pareja['padre1']['nombre']))
                path.append(buscar_pal(pareja['padre2']['nombre']))
                for key in pareja:
                        if key == 'resultado':
                                continue
                        nombre_pal = pareja[key]['nombre']
                        Padre = buscar_pal(nombre_pal)
                        if Padre == inicial:
                                soluciones.append(path.copy())  # Copiar el contenido de path
                        elif limite > 1:
                                lookpath(inicial, objetivo, Padre, limite-1, path)
                path.pop()
                path.pop()
        return 

def mainloop(inicio, objetivo):
        soluciones = []
        path = []
        limite = 1
        path.append(objetivo)
        dot_images = []

        while len(soluciones) == 0 and limite < 5:
                lookpath(inicio, objetivo, objetivo, limite, path)
                limite += 1
        
        limite = 0
        if len(soluciones) == 0:
                path.clear()
                soluciones = []
                return False

        solucionesfiltred = soluciones.copy()
        # eliminando soluciones repetidas
        for sol in soluciones:
                for sol2 in soluciones:
                        i = 1
                        while i < len(sol) - 1 and i < len(sol2):
                                if sol2[i] == sol[i + 1] and sol2[i + 1] == sol[i]:
                                        if sol2 in solucionesfiltred and sol in solucionesfiltred:
                                                solucionesfiltred.remove(sol2)
                                i += 2
        i = 0

        soluciones = solucionesfiltred.copy()

        for sol in soluciones:
                dot = graphviz.Digraph(comment='Genealogical Tree')
                i = len(sol) - 1
                while i > 0:
                        padre1 = sol[i]
                        padre2 = sol[i - 1]
                        hijo = buscar_apareamiento(padre1, padre2)
                        dot.node(padre1[0], label=padre1[0])
                        dot.node(padre2[0], label=padre2[0])
                        dot.node(hijo[0], label=hijo[0])
                        dot.edge(padre1[0], hijo[0])
                        dot.edge(padre2[0], hijo[0])
                        i = i - 2

                png_dot = dot.pipe(format='png')
                dot_images.append(png_dot)  # Agregar el dot al array de imágenes
        
        soluciones.clear()
        path.clear()
        return dot_images