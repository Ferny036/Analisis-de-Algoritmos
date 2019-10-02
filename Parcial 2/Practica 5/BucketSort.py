"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 5b : BucketSort
"""
#*Llamamos a las bibliotecas necesarias
import random
from Graficas import Graphics
time = 0

#! Definicion del algoritmo de BucketSort
def bucketSort(A, b):
    global time
    mayor = max(A); time += 1 #* El elemento mayor del arreglo 
    n = len(A); time += 1 #* Tamaño del arreglo 
    size = mayor/n; time += 1 #* Tamaño que tendra cada bucket
    buckets = [[] for _ in range(n)]; time += 1 #* Definicion de los buckets
    time += 1

    #* Ingreso a los buckets los elementos pertenecientes al rango
    for i in range(n):
        time += 1
        j = int(A[i]/size); time += 1
        if j != n:
            time += 1
            buckets[j].append(A[i]); time += 1
        else:
            time += 1
            buckets[n - 1].append(A[i]); time += 1
    time += 1
    #* Ordenamos cada bucket con InsertionSort
    for i in range(n):
        time += 1
        #if b == True:
            #buckets[i].reverse()
        insertSort(buckets[i])
    result = []; time += 1
    time += 1
    #* Ingresamos cada bucket al nuevo arreglo
    for i in range(n):
        time += 1
        result = result + buckets[i]; time += 1
    return result

#! Definicion del algoritmo auxiliar de Buket que ayuda a ordenar los elementos en cada bucket
def insertSort(A):
    global time
    time += 1
    for i in range(1, len(A)):
        index = A[i]; time += 1
        j = i - 1; time += 1
        time += 1
        while( j >= 0 and A[j] > index):
            A[j + 1] = A[j]; time += 1
            j = j - 1; time += 1
        A[j + 1]  = index; time += 1
    return A

#! Defincion de la funcio que llena el arreglo con valores aleatorios
def llenarAleatorio(A, n):
    for k in range(n):
        A.append(random.randint(4,10000))

#! Funcion que ayuda a determinar los peores casos para Bucket
def PeorCaso(A,n):
    llenarAleatorio(A,n)
    #* Peor caso cuando estan ordenados los elementos al reves
    A.sort()
    A.reverse()
    return bucketSort(A, True)

#! Funcion que ayuda a determinar los mejores casos para Bucket
def MejorCaso(A,n):
    llenarAleatorio(A,n)
    #* Mejor caso cuando estan ordenados los elementos
    A.sort()
    print(A)
    return bucketSort(A, False)

#! Funcion que ayuda a escribir en el archivo los tamaños del arreglo
def escrituraN(n, file):
    for i in range(n):
        impresion(i + 1, file, n - 1, i)
        
#! Funcion que ayuda a distinguir los datos que estaran escritos en el archivo
def impresion(item, file, limit, index):
    #* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(item, file = file, end='\n')
    #* Sino escribe una comida seguida de un espacio
    else: 
        print(item, file = file, end=', ')

#! Definicion de la funcion principal main
def main():
    global time
    A=[]
    file = open("./files_practices/pract_5b.txt", 'w')
    limit = 70

    #* Iteramos para cada tamaño i del arreglo para los peores casos
    for i in range(1,limit):
        n = i
        llenarAleatorio(A,n)
        bucketSort(A, n)
        print("Caso Aleatorio:", A)
        #? Escribimos en cada iteracion el resultado de ordenar
        impresion(time, file, limit - 1, i)
        A.clear()
        time=0
        print("--------------------------------------------------------------------------------")

    escrituraN(n, file)

    #* Iteramos para cada tamaño i del arreglo para los peores casos
    for i in range(1,limit):
        n = i
        A = PeorCaso(A,n)
        print("Peor caso:", A)
        #? Escribimos en cada iteracion el resultado de ordenar
        impresion(time, file, limit - 1, i)
        A.clear()
        time=0
        print("--------------------------------------------------------------------------------")

    escrituraN(n, file)

    # * Iteramos para cada tamaño i del arreglo  para los mejores casos
    for i in range(1,limit):
        n = i
        MejorCaso(A, n)
        print("Mejor caso:", A)
        #? Escribimos en cada iteracion el resultado de ordenar
        impresion(time, file, limit - 1, i)    
        A.clear()
        time=0
        print("--------------------------------------------------------------------------------")
    escrituraN(n, file)
    file.close()

    #*Configuramos la grafica
    title = "BucketSort"
    x_label = "n: Tamaño del arreglo"
    y_label = "t: Tiempo de ejecución"
    big_O = "O(n)"
    theta = "\Theta(n)"
    omega = "\Omega(n)"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/pract_5b.txt")
    graph.graficar(title, x_label, y_label, big_O, theta, omega)


if __name__ == "__main__":
    main()