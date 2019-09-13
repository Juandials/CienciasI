import random

# funciones

def PeorSeleccion(lista,n):

    i = 0
    c = 0
    while i<n-1:
        m = lista[i+1]
        donde = i+1
        j = i+1
        c= c+11
        while j<n:
            if  (m > lista[j]):
                m = lista[j]
                donde = j
            j=j+1
            c=c+8
        if lista[i]>lista[donde]:
            x = lista[i]
            lista[i] = lista[donde]
            lista[donde] = x
        i = i+1
        c = c+12
    c = c+3
    print('    ',lista)
    print('    El experimental : ',c)

def MejorSeleccion(lista,n):
    i = 0
    c = 0
    while i < n - 1:
        m = lista[i + 1]
        donde = i + 1
        j = i + 1
        c = c + 11
        while j < n:
            if (m > lista[j]):
                m = lista[j]
                donde = j
            j = j + 1

        if lista[i] > lista[donde]:
            x = lista[i]
            lista[i] = lista[donde]
            lista[donde] = x
        i = i + 1
        c = c + 12
    c = c + 3
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
n1 = (n*(n-1)-(n-1)-((n-2)*(n-1))/2)*8+23*(n-1)+3
print('    Por formula es : ',n1)
PeorSeleccion(lista,len(lista))

#mejor caso
print('-------------------------------------------')
print('Mejor caso')

n = int(input("Ingrese el n -> "))
lista = [None] * n

for i in range(n):
    lista[i] = n
print('    ', lista)
n2 = 23*(n-1)+3
print('    Por formula es : ',n2)
MejorSeleccion(lista,len(lista))

#Promedio caso
print('-------------------------------------------')
print('Caso promedio')

n = int(input("Ingrese el n -> "))
lista = [None] * n

for i in range(n):
    lista[i] = n-i
print('    ', lista)
n = (n*(n-1)-(n-1)-((n-2)*(n-1))/2)*8+23*(n-1)+3
print('    Por formula es : ',(n1+n2)/2)
PeorSeleccion(lista,len(lista))