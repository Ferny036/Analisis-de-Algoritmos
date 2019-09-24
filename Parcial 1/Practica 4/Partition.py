"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 4a : Partition
"""
#*llamamos a las bibliotecas necesarias
#*llamamos a la funcion Graphics
import random
from Graficas import  Graphics
time = 0
#!Definimos la función Partition y usamos un contador en cada iteracion
def Partition(A,p,r):
    global time

    x = A[r]; time += 1
    i = p - 1; time += 1
    j = p; time+=1
    while(j < r):
        if(A[j] <= x):
            time += 1
            i += 1
            aux=A[i]
            A[i]=A[j]
            A[j]=aux
        j += 1; time+=1
    aux=A[i + 1]; time+=1
    A[i + 1]=A[r]; time+=1
    A[r]=aux; time+=2
    return i+1          
            
#!Definimos una funcion para llenar aleatoriamente el arreglo
def llenarAleatoriamente(A, n):
    for k in range(n):
        A.append(random.randint(4,1000))

#!Definimos la funcion donde se generan los resultados de el peor de los casos
def PResult(limit, file):
    #?Definimos variables globales que ayudaran al conteo
    global time
    A = []
    p = 0
    #*Le damos valores al arreglo para que sea el peor de los casos
    for i in range (limit):
        n = i + 5
        A.clear()
        for j in range(n):
            A.append(10)
        r = n-1
        #*LLamamos Partition con los indices creados
        Partition(A,p,r)
        #*LLamamos impresion con los indices indicados
        impresion(time, file, limit, i + 1)
        time = 0

#!Definimos la funcion donde se generan los resultados en casos aleatorios
def CaAleatorio(limit, file):
    #?Definimos variables globales que ayudaran al conteo
    global time
    A = []
    #*Le damos valores al arreglo para que sean casos aleatorios
    for i in range (limit):
        A.clear()
        p = 0
        n = i + 5
        r = n - 1
        #*LLamamos llenarAleatoriamente
        llenarAleatoriamente(A, n)
        #*LLamamos Partition con los indices creados
        Partition(A,p,r)
        #*LLamamos impresion con los indices indicados
        impresion(time, file, limit, i + 1)
        time = 0

#!Es donde se escribe en un archivo el tamaño del arreglo
def escrituraN(n, file):
    for i in range(n):
        impresion(i + 1, file, n - 1, i)

#! Definicion de la funcion que determina el modo de impresion para los resultado recibidos
def impresion(item, file, limit, index):
    #* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(item, file = file, end='\n')
    #* Sino escribe una comida seguida de un espacio
    else: 
        print(item, file = file, end=', ')

#! Definicion de la funcion main
def main():
    #?Definimos variables globales que ayudaran al conteo
    global time
    #* abrimos el archivo donde guardaremos los datos recolectados 
    file = open("./files_practices/pract_4a.txt", 'w')
    limit = 30

    #* LLamamos las funciones para cada uno de los casos
    CaAleatorio(limit, file)
    escrituraN(limit, file)
    PResult(limit, file)
    escrituraN(limit, file)

    #*Cerramos el archivo
    file.close()
    #*Configuramos la grafica
    title = "Partition"
    x_label = "n: Tamaño del arreglo"
    y_label = "t: Tiempo de ejecución"
    big_O = "n"
    theta = "n"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/pract_4a.txt")
    graph.graficar(title, x_label, y_label, big_O, theta)



if __name__ == "__main__":
    main()


