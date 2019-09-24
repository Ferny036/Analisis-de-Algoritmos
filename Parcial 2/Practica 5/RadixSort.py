import random
from Graficas import Graphics

time = 0

def llenarAleatorioTam(A, n, tam):
    for k in range(n):
        A.append(random.randint(0,tam))

def determinarCasos(A, n, tam):
    global time
    llenarAleatorioTam(A,n, tam)
    d = len(str(max(A)))
    print("A unsorted = ",A)
    RadixSort(A, d)
    print("A sorted =", A)

def escrituraN(n, file):
    for i in range(n):
        impresion(i + 11, file, n - 1, i)
        
def impresion(item, file, limit, index):
    #* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(item, file = file, end='\n')
    #* Sino escribe una comida seguida de un espacio
    else: 
        print(item, file = file, end=', ')

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

def main():
    global time

    file = open("./files_practices/pract_5a.txt", 'w')
    A = []
    tam = 3
    limit = 20
    for i in range(10, limit + 10):
        determinarCasos(A, i, 99999)
        impresion(time, file, limit + 9, i)
        A.clear()
        time = 0
    
    escrituraN(limit, file)

    for i in range(10, limit + 10):
        determinarCasos(A, i, 999)
        impresion(time, file, limit + 9, i)
        A.clear()
        time = 0

    escrituraN(limit, file)

    file.close()

    title = "RadixSort"
    x_label = "n: tamaño del arreglo"
    y_label = "t: tiempo de ejecucion"
    labelO = "\Theta (3n)"
    labelT = "\Theta (5n)"

    graph = Graphics("./files_practices/pract_5a.txt")
    graph.graficar(title, x_label, y_label, labelO, labelT)



if __name__ == "__main__":
    main()