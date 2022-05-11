""" 
Taller 1 
A. Crear una función que genere una lista de 200 numeros aleatorios
B. Crear una función que ordene de menor a mayor la lista generada
"""
from random import randint
Aleatorios= [randint(1,100)for _ in range(200)]
print("Lista de números aleatorios=",Aleatorios)
Ordenados= sorted(Aleatorios)
print("Lista de números ordenada de menor a mayor",Ordenados)
