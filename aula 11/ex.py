from random import sample

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = []

for i in range(5):

    lista_auxiliar = sample(range(0, 100), 5)
    lista.append(lista_auxiliar)
    lista = remove_repetidos(lista)

print(f'A lista é {lista}')