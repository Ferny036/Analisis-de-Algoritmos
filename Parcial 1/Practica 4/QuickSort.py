"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 4b : QuickSort
"""
#*llamamos a las bibliotecas necesarias
#*llamamos a la funcion partition 
import Partition as Part
import random
from Graficas import Graphics
#?Definimos variables globales que ayudaran al conteo
time = 0
totalTime = []
totalSteps = []
#!Definimos la funcion donde se imprimen los resultados obtenidos
def imprimirResultados(file):
    #?Definimos las variables globales para el conteo
    global totalSteps
    global totalTime
    #?Definimos la variable limit donde le asignaremos el valor del tamaño de totalTime
    limit = len(totalTime)
    #*Para todos los valores dentro del valor de limit
    for i in range(limit):
        #*Llamamos a la funcion imprimir con valores obtenidos
        impresion(totalTime[i], file, i, limit - 1)
    #?Definimos la variable limit donde le asignaremos el valor del tamaño de totalSteps
    limit = len(totalSteps)
    #*Para todos los valores dentro del valor de limit
    for i in range(limit):
        #*Llamamos a la funcion imprimir con valores obtenidos
        impresion(totalSteps[i], file, i, limit - 1)


#! Definicion de la funcion que determina el modo de impresion para los resultado recibidos
def impresion(item, file, index, limit):

	#* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(item, file = file, end='\n')
	#* Sino escribe una comida seguida de un espacio
    else: 
        print(item, file = file, end=', ')

#!Definimos Partition para los casos de prueba
def Partition(A, p, r):
    return int((r - p)/2) + p

#!Definimos la funcion de Quicksort donde se obtendran los valores cuando el proceso parte el arreglo por la mitad
def QuickSortMiddle(A, p, r):
    #? Definicion local de la variable global que llevara el conteo total de iteraciones
    global time
    #? Incrementamos 1 a time
    time += 1
    #*Si p < r
    if p < r:
        #? A una variable q le asignaremos el valor obtenido de Partition e incrementamos 1 a time 
        q = Partition(A, p, r); time += r - p
        #* Escribimos los valores importantes del arreglo
        print("p = %d, q = %d, r = %d" % (p,q,r))
        #* llamamos a la funcion QuickSortMidlle con indices difinidose e incrementamos 1 a time en cada iteración
        QuickSortMiddle(A, p, q); time += 1
        QuickSortMiddle(A, q + 1, r); time += 1

#! Definimos la funcion donde se llenara el arreglo con valores aleatorios
def llenarAleatoriamente(A, n):
    for k in range(n):
        A.append(random.randint(4,1000))

#! Definimos la funcion QuickSort
def QuickSort(A, p, r):

    global time
    aux = 0
    time += 1
    if p < r:
        q = Part.Partition(A, p, r, time); time += r - p
        print("p = %d, q = %d, r = %d" % (p,q,r))
        QuickSort(A, p, q - 1); time += 1
        QuickSort(A, q, r); time += 1
#! Definicion de la funcion main o principal que se ejecutara al inicio
def main():
    #? Definicion local de las variable global que llevara el conteo
    global time
    global totalTime
    global totalSteps
    #* Definicion del archivo auxiliar donde escribiremos los resultados
    file = open("./files_practices/pract_4b.txt", 'w')
    #? Definicion local de arreglos
    A_hip = [] 
    A_middle = []
    #*Para todos los valores dentro de 20
    for i in range(20):
        #*Limpiamos el arreglo
        A_middle.clear()
        #*Le damos valores necesarios para crear el arreglo
        n = random.randint(4,30)
        p = 0
        r = n - 1
        llenarAleatoriamente(A_middle,n)
        print("r = %d" % r)
        print("inorder A = ", A_middle)
        #*llamamos quickSortMiddle con los indices que queremos
        QuickSortMiddle(A_middle, p, r)
        #*Agregagamos los valores de las iteraciones
        totalSteps.append(n)
        totalTime.append(time)
        time = 0
        print("order A = ", A_middle)
    
    totalSteps.sort()
    totalTime.sort()
    #*Mandamos a llamar imprimirResultados en el archivo
    imprimirResultados(file)

    totalSteps.clear()
    totalTime.clear()
    print("-------------------------------------------------------------")
    #*Para todos los valores dentro de 20
    for i in range(20):
        #*Limpiamos el arreglo
        A_hip.clear()
        #*Le damos valores necesarios para crear el arreglo
        n = random.randint(4,30)
        r = n - 1
        llenarAleatoriamente(A_hip,n)
        print(A_hip)
        print("r = %d" % r)
        A_hip.sort()
        A_hip.reverse()
        print("inorder A = ", A_hip)
        #*llamamos quickSortMiddle con los indices que queremos
        QuickSort(A_hip, p, r)
        #*Agregagamos los valores de las iteraciones
        totalSteps.append(n)
        totalTime.append(time)
        time = 0
        print("order A = ", A_hip)
    
    totalSteps.sort()
    totalTime.sort()
    #*Mandamos a llamar imprimirResultados en el archivo
    imprimirResultados(file)
    #*Cerramos el archivo
    file.close()
    #*Configuramos la grafica
    title = "QuickSort"
    x_label = "n: Tamaño del array"
    y_label = "t: Tiempo de ejecución"
    big_O = "n^2"
    theta = "n \log (n)"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/pract_4b.txt")
    graph.graficar(title, x_label, y_label, big_O, theta)


if __name__ == "__main__":
    main()