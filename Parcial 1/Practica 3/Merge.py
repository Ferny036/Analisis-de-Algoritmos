"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 3a: "Algoritmo Merge"
"""

#* Llamamos a la bibliotecas necesarias para ejecutar nuestro archivo
from Graficas import Graphics
import numpy as np
import random

#? Definicion de las variables globales a utilizar para implementacion correcta de nuestro algoritmo
time = 0
totalSteps = []
totalTime = []

#! Definicion de la funcion  principal main
def main():
    
    #? Defincion local de las variables globales
    global totalTime
    global totalSteps

    #* Establecemos un limite de evaluaciones de Merge
    limit = 25

    #? Abrimos el archivo en modo escritura donde escribiremos los resultados de las iteraciones
    file = open("./files_practices/pract_3.txt", 'w')

    #* Repetimos el algoritmo limit-veces llenandolo aleatoriamente
    for i in range(2,limit + 2):
        llenadoAleatorio(i)

    #? Ordenamos las listas para poderlas graficar mejor
    totalTime.sort()
    totalSteps.sort()

    #? Imprimimos en el archivo los resultados totales del programa
    for j in range(limit):
        impresion(file,j,totalTime[j],limit- 1)
    
    for j in range(limit):
        impresion(file,j,totalSteps[j],limit- 1)
    
    for j in range(limit):
        impresion(file,j,totalTime[j],limit- 1)

    #* Cerramos el archivo
    file.close()

    #* Llamamos al objeto que nos permite graficar
    graph = Graphics("./files_practices/pract_3.txt")
    graph.graficar("Merge","n: Tamaño del Arreglo","t: Número de Iteraciones", "n")

#! Defincion de la funcion que llama a merge con un tamaño aleatorio
def llenadoAleatorio(index):
    
    #? Definicion local de las variables globales
    global time
    global totalSteps
    global totalTime

    #*  Definimos nuestras variables a utilizar
    A = []
    aux = []
    #? Ingresamos el tamaño del array a la lista de tamaños
    tam = index*2
    totalSteps.append(tam)

    #* Llenamos aleatoriamente la lista y la ordenamos, mitad ordenada y mitad ordenada
    llenarAleatorio(A, 0, int(tam/2) - 1)
    llenarAleatorio(A, int(tam/2), tam - 1)

    #* Imprmimos en consola el array a ordenar y obtenemos el tamaño total del array y se lo asignamos a r
    print("A before sort := ", A)
    r = len(A) - 1

    #? Llamamos a la funcion principal de Merge y obtenemos el numero de iteraciones realizadas
    time = Merge(A, 0, int(r/2), r, True)
    #? El resultado lo almacenamos en la lista de tiempos
    totalTime.append(time)
    #? Reiniciamos el contador global
    time = 0


#! Definicion de la funcion que determina el tipo de impresion en un archivo
def impresion(file, n, t, limit):

    #* Si es el ultimo elemento lo imprime con un salto de linea
    if(n == limit):
        print(t, file=file, end="\n")
    #* Sino escribe el elemento actual seguido de una coma y un espacio
    else:
        print(t, file= file, end=", ")

#! Definicion de la funcion que llena con numeros aleatorios la lista de forma ordenada en una mitad
def llenarAleatorio(A, p, q):
    #* Defincion de un array auxiliar que almacenara los valores aleatorios obtenidos
    aux = []

    #* Para todos los valores entre p y q, ingresa en aux un valor entre 0 y 1000 aleatoriamente
    for i in range(p, q, 1):
        aux.append(random.randint(0, 1000))
    
    #* Ordena la lista aux
    aux.sort()

    #* Ingresa los valores de aux a la lista principal
    for j in range(p, q, 1):
        A.append(aux[j - p])


#! Definicion formal del algoritmos Merge
def Merge(A, p, q, r, val):

    time = 0
    
    n = q - p + 1; time += 1
    m = r - q; time += 1
    
    I=[0]*n; time += 1
    D=[0]*m; time += 1
    i = 0; time += 1
    j = 0; time += 1

    time += 1
    while i < n:
        I[i]=A[p+i]; time += 1
        i += 1; time += 1
    time += 1
    while j < m:
        D[j]=A[q+j+1]; time += 1
        j += 1; time += 1

    time += 1
    if val:
        I.sort(); time += 1
        D.sort(); time += 1
    
    print("I = ", I)
    print("D = ", D)

    i = j = 0; time += 1

    k = p; time += 1
    while(True):
        time += 1
        if i < n and j < m:
            time += 1
            if I[i]<=D[j]:

                A[k]=I[i]; time += 1
                i+=1; time += 1
            else:

                A[k]=D[j]; time += 1
                j+=1; time += 1
            k+=1; time += 1
        else:
            time += 1
            if i >= n:
                time += 2
                while(j < len(D)):
                    A[k] = D[j]; time += 1
                    k += 1; time += 1
                    j += 1; time += 1
            elif j >= m:
                time += 2
                while(i < len(I)):
                    A[k] = I[i]; time += 1
                    k += 1; time += 1
                    i += 1; time += 1
                
            print("A after sort: ",A, end='\n--------------------------------------\n\n')
            return time
            break

#* Llamada a la funcion main, si se ejecuta desde consola el archivo Merge.py en lugar de Merge-Sort.py
if __name__ == "__main__":
    main()