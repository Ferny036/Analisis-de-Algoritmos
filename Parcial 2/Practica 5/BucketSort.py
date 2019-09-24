import numpy as np
import random
from Graficas import Graphics
time = 0

def bucketSort(A):
    global time
    mayor = max(A); time += 1
    n = len(A); time += 1
    size = mayor/n; time += 1
    buckets = [[] for _ in range(n)]; time += 1
    time += 1
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
    for i in range(n):
        time += 1
        insertSort(buckets[i])
    result = []; time += 1
    time += 1
    for i in range(n):
        time += 1
        result = result + buckets[i]; time += 1
    return result


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

def llenarAleatorio(A, n):
    for k in range(n):
        A.append(random.randint(4,100))

def PeorCaso(A,n):
    global time
    llenarAleatorio(A,n)
    A.sort()
    A.reverse()
    print(A)
    bucketSort(A)

def MejorCaso(A,n):
    global time
    llenarAleatorio(A,n)
    A.sort()
    print(A)
    bucketSort(A)


def escrituraN(n, file):
    for i in range(n):
        impresion(i + 1, file, n - 1, i)
        
def impresion(item, file, limit, index):
    #* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(item, file = file, end='\n')
    #* Sino escribe una comida seguida de un espacio
    else: 
        print(item, file = file, end=', ')

def main():
    A=[]
    file = open("./files_practices/pract_5b.txt", 'w')
    limit = 20
    for i in range(limit):
        A.append(1)
    print(A)
    insertSort(A)
    print("A ordened:", A)

"""
def main():
    global time
    A=[]
    file = open("./files_practices/pract_5b.txt", 'w')
    limit = 20

    for i in range(1,limit):
        n = i
        PeorCaso(A,n)
        print("Peor caso:", A)
        impresion(time, file, limit - 1, i)
        A.clear()
        time=0
        print("--------------------------------------------------------------------------------")
    escrituraN(n, file)
    for i in range(1,limit):
        n = i
        MejorCaso(A,n)
        print("Mejor caso:", A)
        impresion(time, file, limit - 1, i)    
        A.clear()
        time=0
        print("--------------------------------------------------------------------------------")
    escrituraN(n, file)
    
    print("",A)
    file.close()
    #*Configuramos la grafica
    title = "BucketSort"
    x_label = "n: Tamaño del arreglo"
    y_label = "t: Tiempo de ejecución"
    big_O = "\Theta(n)"
    theta = "\Theta(n)"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/pract_5b.txt")
    graph.graficar(title, x_label, y_label, big_O, theta)
"""


if __name__ == "__main__":
    main()