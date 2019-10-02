from Graficas import Graphics
import random
time = 0

def MSC(A, bajo, mitad, alto, t):

    suma = 0; t += 1
    n = alto - bajo + 1; t += 1
    suma_izq = -((4**5)**5); t += 1
    max_izq = suma_izq; t += 1
    t += 1
    for i in range(mitad - 1, bajo - 1, -1):
        t += 1
        suma = suma + A[i] ; t += 1
        t += 1
        if suma > suma_izq:
            suma_izq = suma ; t += 1
            max_izq=i;t += 1
    suma = 0; t += 1
    suma_der = 0 ; t += 1
    max_der = mitad ; t += 1
    t += 1
    for i in range(mitad, alto):
        suma = suma + A[i]; t += 1
        t += 1
        if suma > suma_der:
            suma_der = suma ; t += 1
            max_der = i ; t += 1
    t += 1
    time = t
    return (t, max_izq, max_der, suma_izq + suma_der)

def llenarAleatorio(A, n):
    for k in range(n):
        A.append(random.randint(-100,100))

def mejorCaso(A, n, bajo, mitad, alto, file, limit):
    global time
    for i in range(1, n + 1):
        A.append(-i)
    time, a, b, c =  MSC(A, bajo, mitad, alto, time)
    print("Mejor Caso", a, b, c)
    A.clear()
    impresion(time,file, limit - 1, n)
    time = 0

def peorCaso(A, n, bajo, mitad, alto, file, limit):
    global time
    for i in range(1, n + 1):
        A.append(i*10)
    time, a, b, c =  MSC(A, bajo, mitad, alto, time)
    print("Peor Caso:", a, b, c)
    A.clear()
    impresion(time,file, limit - 1, n)
    time = 0

def casoAleatorio(A, n, bajo, mitad, alto, file, limit):
    global time
    llenarAleatorio(A, n)
    time, a, b, c =  MSC(A, bajo, mitad, alto, time)
    print(a, b, c)
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
    file = open("./files_practices/Practica_6a.txt", 'w')
    A = []
    limit = 50
    alto=limit
    mitad=int(limit/2)
    bajo=0

    for i in range(1, limit + 1):
        alto=i
        mitad=int(i/2)
        casoAleatorio(A, i, bajo, mitad, alto, file,  limit + 1)
    escrituraN(limit, file)

    for i in range(1, limit + 1):
        alto=i
        mitad=int(i/2)
        peorCaso(A, i, bajo, mitad, alto, file,  limit + 1)
    escrituraN(limit, file)

    for i in range(1, limit + 1):
        alto=i
        mitad=int(i/2)
        mejorCaso(A, i, bajo, mitad, alto, file, limit + 1)
    escrituraN(limit, file)
    
    file.close()
    
    #* Configuracion de la graficas
    title = "Maximo SubArreglo Cruzado"
    x_label = "n: Tamaño del arreglo"
    y_label = "t: Tiempo de ejecución"
    big_O = "O(n)"
    omega = "\Omega(n)"
    theta = "\Theta(n)"
    #* Graficamos los resultados
    graph = Graphics("./files_practices/Practica_6a.txt")
    graph.graficar(title, x_label, y_label, big_O, theta, omega)

if __name__ == "__main__":
    main()