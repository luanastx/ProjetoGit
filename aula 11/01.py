from random import randint
import random
import numpy as np

matriz = []

for x in range(1, 11):

    lista = []

    for y in range(1, 11):
        lista.append(random.randint(1, 20))

    print('---adicionando a lista---')
    print(lista)
    matriz.append(lista)
#a
matriz = np.sum(matriz)  

print('---soma da matriz---')
print(matriz)  

#b
matrizB = []

for x in range(1, 5):
    listaB = []

    for y in range(1, 6):
        listaB.append(matriz *3)


    print('---adicionando a lista da matrizB---')
    print(listaB)
    matrizB.append(listaB)
 
print('---matriz---')
print(matrizB)


