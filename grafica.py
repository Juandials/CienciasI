import random
from math import log
from tkinter import *
from tkinter import Canvas
def grafica (m,opsEl):
    l1 = Label(m)
    l1.pack()
    l1.place(x=10 , y=0)
    lienzo = Canvas(m, width=500, height=500)
    lienzo.pack()
    lienzo.place(x=10,y=10)
    lienzo.create_line(1,0,1,300, fill='red')
    lienzo.create_line(0,250,500,250, fill='red')
    x=0.1
    while x<1000:
        posy = log(x,2)
        posy = posy*4
        lienzo.create_line(x,250-posy,x,250-posy+1, fill='blue')
        x += 0.1
    for n in range(len(opsEl)-1):
        posY = opsEl[n]
        posY2 = opsEl[n+1]
        lienzo.create_line((10*(n)),250-posY,(10*(n+1)),250-posY2, fill='green')        
def buscarNumero(numeros,izquierda,derecha,llave,c):
    if izquierda==derecha:
        c[0] += 1
        encontrado = numeros[izquierda] == llave
        c[0] += 2
    else:
        mitad = (izquierda+derecha) // 2;
        c[0] += 3
        if numeros[mitad] == llave:
            c[0] += 2
            encontrado = mitad
            c[0] += 1
        elif numeros[mitad] < llave:
            c[0] += 4
            encontrado = buscarNumero(numeros, mitad + 1, derecha, llave,c)
        elif numeros[mitad] > llave:
            c[0] += 4
            encontrado = buscarNumero(numeros, izquierda, mitad - 1, llave,c)    
    return (c[0])

 
def generarNumeros(n):
    numeros = [0]*n
    for i in range(n):
        numeros[i]= random.randrange(99)
    return numeros   
def ordenarNumeros(numeros):
    for i in range (len(numeros)-1):
        for j in range(i+1,len(numeros)):
            if numeros[i] > numeros[j]:
                temp = numeros[i]
                numeros[i] = numeros[j]
                numeros[j] = temp
    return numeros
def generarIndice(n):
    indice = random.randrange(n)
    print(indice)
    return indice


n = int(input("digite cantidad de iteraciones: "))
opsEl = [0]*n
for i in range(n):
    numeros = generarNumeros(n)
    c = list(range(n))
    c[0] = 0
    llave = numeros[generarIndice(n)]
    numeros= ordenarNumeros(numeros)
    oe = buscarNumero(numeros,0,len(numeros),llave,c)
    opsEl[i] = oe

marco = Tk()
marco.title('Dibujar gráfica')
marco.geometry("550x400")
menubar = Menu(marco)
marco.config(menu = menubar)
horizontal = Menu(marco, tearoff=0)
horizontal.add_command(label="graficar",command=lambda:grafica(marco,opsEl))
menubar.add_cascade(label="funcion",menu=horizontal)
marco.mainloop()



    
