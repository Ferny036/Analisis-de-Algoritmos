"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 5c : CocktailSrot
"""
#* Llamamos a las bibliotecas necesarias
import random
from Graficas import Graphics

time = 0
#! Definicion del algoritmo de ordenamiento CocktailSort
def CocktailSort(A):
    global time
    n = len(A); time += 1
    combinado = True ; time += 1
    inicio = 0 ; time += 1
    final = n-1; time += 1
    time += 1
    while(combinado == True):
        combinado = False; time += 1
        time += 1
        for i in range(inicio, final):
            time += 1
            if(A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i] ; time += 1
                combinado = True; time += 1
        if(combinado == False):
            break ; time += 1
        combinado = False; time += 1
        final=final-1; time += 1
        time += 1
        for i in range(final - 1, inicio - 1, - 1):
            time += 1
            if(A[i]>A[i+1]):
                A[i], A[i + 1] = A[i + 1], A[i] ; time += 1
                combinado = True; time += 1
        inicio = inicio + 1; time += 1

#! Funcion que ayuda a llenar el arreglo con numeros aleatorios
def llenarAleatorio(A,n):
    for k in range(n):
        A.append(random.randint(4,1000))

#! Funcion que ayuda a obtener los resultados de los peores casos
def PeorCaso(A,n):
    global time
    llenarAleatorio(A,n)
    print(A)
    A.sort()
    A.reverse()
    CocktailSort(A)

#! Funcion que ayuda a obtener los resultados de los mejores casos
def MejorCaso(A,n):
    global time
    llenarAleatorio(A,n)
    print(A)
    A.sort()
    CocktailSort(A)

#! Funcion que escribe en el archivo los diferentes tamaños de los arreglos experimentados
def escrituraN(n, file):
    for i in range(n):
        impresion(i + 1, file, n - 1, i)
        
#! Funcion que ayuda a distinguir el elemento que se escribira en el archivo 
def impresion(item, file, limit, index):
    #* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(item, file = file, end='\n')
    #* Sino escribe una comida seguida de un espacio
    else: 
        print(item, file = file, end=', ')

#! Definicion de la funcion main
def main():
    global time
    A=[]
    file = open("./files_practices/pract_5c.txt", 'w')
    limit = 19
    #* Determinamos los mejores casos para los peores casos
    for i in range(1,20):
        n=i
        llenarAleatorio(A,n)
        CocktailSort(A)
        print("Caso aleatorio:", A)
        impresion(time, file, limit, i)
        A.clear()
        time=0
    escrituraN(n, file)

    #* Determinamos los mejores casos para los peores casos
    for i in range(1,20):
        n=i
        PeorCaso(A,n)
        print("Peor caso:", A)
        impresion(time, file, limit, i)
        A.clear()
        time=0
    escrituraN(n, file)

    #* Determinamos los mejores casos para los mejores casos
    for i in range(1,20):
        n=i
        MejorCaso(A,n)
        print("Mejor caso:", A)
        impresion(time, file, limit, i)    
        A.clear()
        time=0
    escrituraN(n, file)

    file.close()
    #* Configuracion de la graficas
    title = "CockTailSort"
    x_label = "n: Tamaño del arreglo"
    y_label = "t: Tiempo de ejecución"
    big_O = "O(n^2)"
    omega = "\Omega(n)"
    theta = "\Theta(n)"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/pract_5c.txt")
    graph.graficar(title, x_label, y_label, big_O, theta, omega)
    

if __name__ == "__main__":
    main()