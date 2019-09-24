"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 3b: "Merge-Sort"
"""

#* Llamada a las bibliotecas principales para que funcione nuestro programa
#! /usr/bin/env python
from Graficas import Graphics
import random
import Merge as M
import sys

#? Definicion de nuestra variable global que llevara el conteo
time = 0

#! Definicion formal de la funcion Merge Sort que utilizaremos
def Merge_Sort(A, p, r):

    global time
    
    time += 1
    if p < r and r != 0:
        q = int((p+r)/2); time += 1
        Merge_Sort(A, p, q)
        Merge_Sort(A, q + 1, r)
        time += M.Merge(A, p, q, r, False)
    return A

#! Definicion de la funcion que inicializa el arreglo con numeros ya sea aleatorios o secuenciales
def inicializarArreglo(A, n, val):
    
    #* Dependiendo del valor de val(True o False), define si se llenara el arreglo con valores aleatorios
    if val:
        #* Si su valor es True, llenara el array con valores aleatorios
        for i in range(n):
            A.append(random.randint(1, 100))
    else:
        #* Si su valor es False, llenara el array con valores al peor caso
        peoresCasos(A, n)
    return  A

#! Definicion de la funcion main o principal que se ejecutara al inicio
def main():

    #? Definicion local de la variable global que llevara el conteo
    global time
    
    #* Establecemos un limite de casos a evaluar
    limit = 22

    #* Definicion del archivo auxiliar donde escribiremos los resultados
    file = open("./files_practices/pract_3.txt", 'w')
    
    #* Llenamos el arreglo con casos aleatorios hasta limit-iteraciones y los imprimimos en el archivo
    casosAleatoriosMerge(limit, file)

    #* Imprimimos los valores obtenido en el archivo
    for i in range(limit):
        impresion(file, 2*(i + 1), 2*(i + 1), limit * 2)
    
    #* Llenamos el arreglo con los peores casos hasta limit-iteraciones y los imprimimos en el archivo
    peoresCasosMerge(limit, file)

    #* Cerramos el archivo
    file.close()

    #* Graficamos los resultados
    grafico = Graphics("./files_practices/pract_3.txt")
    grafico.graficar("Merge-Sort", "n: Tamaño del arreglo", "t: numero de iteraciones realizadas", "nlog(n)")

#! Definicion de la funcion que determina el tipo de impresion en un archivo
def impresion(file, n, t, limit):

    #* Si es el ultimo elemento lo imprime con un salto de linea
    if(n == limit):
        print(t, file=file, end="\n")
    #* Sino escribe el elemento actual seguido de una coma y un espacio
    else:
        print(t, file= file, end=", ")

#! Definicion de la funcion que ejecuta limit-veces el algoritmo Merge Sort
def casosAleatoriosMerge(limit, file):

    #? Definicion local de la variable global
    global time
    
    #* Por cada 2n tamaños del arreglo
    for n in range(2, (limit * 2) + 2, 2):
        #* Inicia el arreglo aleatoriamente
        A = []
        A = inicializarArreglo(A, n, True)
        r = n
        p = 0

        #* Llamamos a la funcion principal de Merge Sort con el arreglo Inicializado aleatoriamente
        print("A before to sort: ", A)
        Merge_Sort(A, p, r - 1)

        #? El resultado del total de iteraciones lo escribimos en el archivo
        print("A later to sort: ", A)
        impresion(file, n, time,limit * 2)

        #? Reiniciamos el contador global
        time = 0

#! Definicion de la funcion que llena el arreglo con peores casos para Merge Sort
#! Al parecer se cumple para todo tamaño donde n = log2(k)
def peoresCasosMerge(limit, file):

    #? Definicion local de la variable global
    global time

    #* Por cada 2n tamaños de arreglo
    for n in range(2, (limit * 2) + 2, 2):
        #* Inicializa el arreglo con los peores casos 
        A = []
        A = inicializarArreglo(A, n, False)
        r = n
        p = 0

        #* Llama a la funcion principal de Merge Sort
        Merge_Sort(A, p, r - 1)

        #? El resultado de las iteraciones las escribimos en el archivo
        impresion(file, n, time,limit * 2)

        #? Reiniciamos el contador global
        time = 0

#! Definicion de la funcion que determina los peores casos para Merge Sort
def peoresCasos(A,n):
    
    #* Defincion de variables locales auxiliares
    j = 0
    k = 1
    m = n

    #* Para todos los elementos del Array
    for i in range(int(n/2)):

        #* Si el apuntador izquierdo es par
        if (j % 2) == 0:
            #* Ingresalo al Array al final el valor actual 
            A.append(m)
            #* Recorremos el apuntador derecho en valor -2
            m-= 2
            #* K le damos un valor impar creciente y lo agregamos al array
            k = 2*i + 1
            A.append(k)
        #* Si el apuntado izquierdo es impar
        else:
            #* K le damos un valor impar creciente y lo agregamos al array
            k = 2*i + 1
            A.append(k)
            #* Tambien ingresamos el valor del apuntador 
            A.append(m)
            m -= 2
        #* Incrementamos el apuntador izquierdo del array
        j += 1
        
    return A

main()