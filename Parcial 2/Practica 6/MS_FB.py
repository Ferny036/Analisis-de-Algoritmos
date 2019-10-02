import random
import MSC
from Graficas import Graphics
time = 0

def MS(A):
    global time
    suma_max = 0 ; time += 1
    suma = 0 ; time += 1
    n = len(A) ;  time += 1
    time += 1
    for i in range(n):
        time += 1
        for j in range(i,n):
            suma += A[j] ; time += 1
            time += 1
            if suma > suma_max:
                suma_max = suma ; time += 1
    
    return suma_max
        
def llenarAleatorio(A, n):
    for k in range(n):
        A.append(random.randint(-100,100))

def mejorCaso(A, n, file, limit):
    global time
    for i in range(1, n + 1):
        A.append(-i)
    print("Mejor Caso", MS(A))
    A.clear()
    impresion(time,file, limit - 1, n)
    time = 0

def peorCaso(A, n, file, limit):
    global time
    for i in range(1, n + 1):
        A.append(i)
    print("Peor Caso:", MS(A))
    A.clear()
    impresion(time,file, limit - 1, n)
    time = 0

def casoAleatorio(A, n, file, limit):
    global time
    llenarAleatorio(A, n)
    print("Caso Aleatorio: ",MS(A))
    A.clear()
    impresion(time,file, limit - 1, n)
    time = 0

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


def main():
    global time 
    file = open("./files_practices/Practica_6c.txt", 'w')
    A = []
    limit = 35
    bajo = 0

    for i in range(1, limit + 1):
        alto=i - 1
        mitad=int(i/2)
        casoAleatorio(A, i, file, limit + 1)
    escrituraN(limit, file)

    for i in range(1, limit + 1):
        alto=i - 1
        mitad=int(i/2)
        peorCaso(A, i, file, limit + 1)
    escrituraN(limit, file)

    for i in range(1, limit + 1):
        alto=i - 1
        mitad=int(i/2)
        mejorCaso(A, i, file, limit + 1)
    escrituraN(limit, file)


    file.close()
    
    #* Configuracion de la graficas
    title = "Maximo SubArreglo por Fuerza Bruta"
    x_label = "n: Tamaño del arreglo"
    y_label = "t: Tiempo de ejecución"
    big_O = "O(n^2)"
    omega = "\Omega(n^2)"
    theta = "\Theta(n^2)"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/Practica_6c.txt")
    graph.graficar(title, x_label, y_label, big_O, theta, omega)



if __name__ == "__main__":
    main()