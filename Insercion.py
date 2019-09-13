import random

# funciones

def PeorInsercion(lista,n):

    j = 0
    c = 1
    for i in range(1,n):
        c = c + 2
        aux = lista[i]
        j = i - 1
        c = c + 4
        while (j >= 0 and aux < lista[j]):
            c = c + 4
            lista[j+1] = lista[j]
            j = j-1
            c= c+5
        c = c+4
        lista[j + 1] = aux
        c = c + 3
    c = c + 1

    print('    ', lista)
    print('    El experimental : ', c)

def MejorInsercion(lista,n):

    j = 0
    c = 1
    for i in range(1, n):
        c = c + 2
        aux = lista[i]
        j = i - 1
        c = c + 8
        while (j >= 0 and aux < lista[j]):
            c = c + 4
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = aux
        c = c + 3
    c = c + 1

    print('    ', lista)
    print('    El experimental : ', c)

# Programa Principal

print('METODO DE SELECCION')

#Peor caso
print('-------------------------------------------')
print('Peor caso')

n = int(input("Ingrese el n -> "))
lista = [None] * n

for i in range(n):
    lista[i] = n-i
print('    ', lista)
n1 = 2+13*(n-1)+9*((n*(n-1))/2)
print('    Por formula es : ',n1)
PeorInsercion(lista,len(lista))

#mejor caso
print('-------------------------------------------')
print('Mejor caso')

n = int(input("Ingrese el n -> "))
lista = [None] * n

for i in range(n):
    lista[i] = i
print('    ', lista)
n2 = 13*(n-1) + 2
print('    Por formula es : ',n2)
PeorInsercion(lista,len(lista))

#Promedio caso
print('-------------------------------------------')
print('Caso promedio')

n = int(input("Ingrese el n -> "))
lista = [None] * n

for i in range(n):
    lista[i] = n-i
print('    ', lista)
n = 2 + 13*(n-1) + 4.5*((n*(n-1))/2)
print('    Por formula es : ',(n1+n2)/2)
PeorInsercion(lista,len(lista))