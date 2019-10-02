import random
import MSC
from Graficas import Graphics
time = 0

def MS(A, bajo, alto):
    global time
    time += 1
    if bajo == alto:
        time += 1        
        return(bajo, alto, A[bajo])
    else:
        time += 1
        mitad=int((bajo + alto)/2);time += 1
        min_izq, max_izq, suma_izq = MS(A, bajo, mitad);time += 1
        min_der, max_der, suma_der = MS(A, mitad + 1, alto);time += 1
        time, min_cruz, max_cruz, suma_cruz = MSC.MSC(A, bajo, mitad, alto + 1, time);time += 1
        #print("------------------------------------------------------")
        time += 1
        if suma_izq > suma_der and suma_izq > suma_cruz:
            #print("izq = %s, cruz = %s, der = %s"%(suma_izq, suma_cruz, suma_der))
            #print("retorno: index_min = %s, index_max = %s, suma = %s"%(min_der, max_der, suma_der))
            time += 1
            return(min_izq, max_izq, suma_izq)
        elif suma_der > suma_izq and suma_der > suma_cruz:
            time += 2
            #print("izq = %s, cruz = %s, der = %s"%(suma_izq, suma_cruz, suma_der))
            #print("retorno: index_min = %s, index_max = %s, suma = %s"%(min_der, max_der, suma_der))
            return(min_der, max_der, suma_der)
        else:
            time += 1
            #print("izq = %s, cruz = %s, der = %s"%(suma_izq, suma_cruz, suma_der))
            #print("retorno: index_min = %s, index_max = %s, suma = %s"%(min_der, max_der, suma_der))
            return(min_cruz, max_cruz, suma_cruz)
        
def llenarAleatorio(A, n):
    for k in range(n):
        A.append(random.randint(-100,100))

def mejorCaso(A, n, bajo, mitad, alto, file, limit):
    global time
    for i in range(1, n + 1):
        A.append(-i)
    print("Mejor Caso", MS(A, bajo, alto))
    A.clear()
    impresion(time,file, limit - 1, n)
    time = 0

def peorCaso(A, n, bajo, mitad, alto, file, limit):
    global time
    for i in range(1, n + 1):
        A.append(i)
    print("Peor Caso:", MS(A, bajo, alto))
    A.clear()
    impresion(time,file, limit - 1, n)
    time = 0

def casoAleatorio(A, n, bajo, mitad, alto, file, limit):
    global time
    llenarAleatorio(A, n)
    print("Caso Aleatorio: ",MS(A, bajo, alto))
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
    file = open("./files_practices/Practica_6b.txt", 'w')
    A = []
    limit = 35
    bajo = 0

    for i in range(1, limit + 1):
        alto=i - 1
        mitad=int(i/2)
        casoAleatorio(A, i, bajo, mitad, alto, file,  limit + 1)
    escrituraN(limit, file)

    for i in range(1, limit + 1):
        alto=i - 1
        mitad=int(i/2)
        peorCaso(A, i, bajo, mitad,  alto, file,  limit + 1)
    escrituraN(limit, file)

    for i in range(1, limit + 1):
        alto=i - 1
        mitad=int(i/2)
        mejorCaso(A, i, bajo, mitad,  alto, file,  limit + 1)
    escrituraN(limit, file)


    file.close()
    
    #* Configuracion de la graficas
    title = "Maximo SubArreglo"
    x_label = "n: Tamaño del arreglo"
    y_label = "t: Tiempo de ejecución"
    big_O = "O(n\log(n))"
    omega = "\Omega(n\log(n))"
    theta = "\Theta(n\log(n))"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/Practica_6b.txt")
    graph.graficar(title, x_label, y_label, big_O, theta, omega)



if __name__ == "__main__":
    main()