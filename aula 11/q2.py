from random import random, sample
from random import randint
import random
lista = []


for i in range(5):
    lista_auxiliar = sample(range(0,100), 5)
    lista.append(lista_auxiliar)

    for linha in lista:
            if linha == lista:
                print(lista)
            else:
                lista.append(random.randint(0,20))

for coluna in lista:
    if coluna == lista:
        print(lista)
    else:
        lista.append(random.randint(0,20))
        
print(f'a lista é {lista}')
