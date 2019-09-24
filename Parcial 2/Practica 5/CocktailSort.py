import random

time = 0
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

def llenarAleatorio(A,n):
    for k in range(n):
        A.append(random.randint(4,1000))

def PeorCaso(A,n):
    global time
    llenarAleatorio(A,n)
    print(A)
    A.sort()
    A.reverse()
    CocktailSort(A)

def MejorCaso(A,n):
    global time
    llenarAleatorio(A,n)
    print(A)
    A.sort()
    CocktailSort(A)

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
    global time
    A=[]
    file = open("./files_practices/pract_5c.txt", 'w')
    limit = 19
    for i in range(1,20):
        n=i
        PeorCaso(A,n)
        print("Peor caso:", A)
        impresion(time, file, limit, i)
        A.clear()
        time=0
    escrituraN(n, file)
    for i in range(1,20):
        n=i
        MejorCaso(A,n)
        print("Mejor caso:", A)
        impresion(time, file, limit, i)    
        A.clear()
        time=0
    escrituraN(n, file)
if __name__ == "__main__":
    main()