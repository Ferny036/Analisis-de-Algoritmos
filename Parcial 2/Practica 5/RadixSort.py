"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 5a : RadixSort
"""
#* Llamamos a las bibliotecas necesarias
import random
from Graficas import Graphics

time = 0

#! Funcion que llena el arreglo con numeros aleatorios de tamaño tam
def llenarAleatorioTam(A, n, tam):
    for k in range(n):
        A.append(random.randint(0,tam))

#! Funcion que ayuda  adterminar el peor y mejor de los casos para Radix (Aunque sea Theta)
def determinarCasos(A, n, tam):
    global time
    llenarAleatorioTam(A,n, tam)
    d = len(str(max(A)))
    print("A unsorted = ",A)
    RadixSort(A, d)
    print("A sorted =", A)

#! Funcion que escribe en el archivo los tamaños de los arreglos
def escrituraN(n, file):
    for i in range(n):
        impresion(i + 11, file, n - 1, i)
        
#! Funcion que ayuda a distinguir lo que se escribira en el archivo
def impresion(item, file, limit, index):
    #* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(item, file = file, end='\n')
    #* Sino escribe una comida seguida de un espacio
    else: 
        print(item, file = file, end=', ')

#! Definicion de la funcion Radix 
def RadixSort(A, d):
    global time

    n = len(A); time += 1
    posDigit = 1; time += 1
    result = []; time += 1
    llenarAleatorioTam(result, n, 1) ; time += 1
    time += 1
    for j in range(1,d + 1):
        
        count = []; time += 1
        time += 1
        for i in range(n):
            count.append(0);time += 1

        time += 1
        for i in range(n):
            count[int(A[i]/posDigit) % 10] += 1; time += 1
        
        time += 1
        for i in range(1, 10):
            count[i] += count[i - 1];time += 1
        
        time += 1
        for i in range(n - 1, -1, -1):
            result[count[ int(A[i]/posDigit)%10 ] - 1] = A[i]; time += 1
            count[ int(A[i]/posDigit)%10 ] -= 1; time += 1
        
        time += 1
        for i in range(n):
            A[i] = result[i]; time += 1

        posDigit *= 10 ; time += 1

#! Definicion de la funcion main
def main():
    global time

    file = open("./files_practices/pract_5a.txt", 'w')
    A = []
    tam = 3
    limit = 20

    #* Elejimos los mejores casos 
    for i in range(10, limit + 10):
        determinarCasos(A, i, 9999)
        impresion(time, file, limit + 9, i)
        A.clear()
        time = 0
    escrituraN(limit, file)

    #* Elejimos los peores casos
    for i in range(10, limit + 10):
        determinarCasos(A, i, 9999999999)
        impresion(time, file, limit + 9, i)
        A.clear()
        time = 0
    
    escrituraN(limit, file)


    #* Elejimos los mejores casos 
    for i in range(10, limit + 10):
        determinarCasos(A, i, 9)
        impresion(time, file, limit + 9, i)
        A.clear()
        time = 0
    escrituraN(limit, file)


    file.close()

    #* Configuramos las graficas
    title = "RadixSort"
    x_label = "n: tamaño del arreglo"
    y_label = "t: tiempo de ejecucion"
    labelO = "\Theta (10n)"
    labelT = "\Theta (3n)"
    labelOm = "\Theta (1n)"

    graph = Graphics("./files_practices/pract_5a.txt")
    graph.graficar(title, x_label, y_label, labelO, labelT, labelOm)



if __name__ == "__main__":
    main()