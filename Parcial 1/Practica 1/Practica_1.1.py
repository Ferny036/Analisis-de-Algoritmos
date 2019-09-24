"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 1a : "Suma  de numeros binarios"
"""

#* Llamada a bibliotecas externas para uso de números aleatorios
import random
import sys
from Graficas import Graphics

#? Declaracion de los arrays globales que guardaran los resultados de t y n
totalTime = []
totalSteps = []

#! Definicion de la funcion que prepara los arrays a sumar y recibe el
#! resultado final de la misma
def preSumaBinaria(k):
    #* Establece el tamaño de n = 2^k o equivalentemente k = log2(n)
    n = 2**k;
    #? Agregamos el valor actual de n al array global
    totalSteps.append(n)
    
    #* Declaracion de los arreglos de a sumar y el de resultado
    C = []

    #* Declaracion e inicializacion de una variable que funcionara como corrimiento
    Z = 0
    
    #* Llamamos a la funcion para darle valores alreatorios a cada elemento de
    #* los arrays a sumar
    K, T = inicializarListas(n, 0)
    
    #* Llamamos a la funcion que realizara la suma binaria la cual retorna
    #* un array con la suma realizada
    C = sumaBinaria(K, T, Z)

    #* Reacomodamos alreves los elementos de los arrays a sumar 
    K = list(reversed(K))
    T = list(reversed(T))

    #* Acomodamos nuevamente al reves los elementos del array resultado
    C = list(reversed(C))

    #* Imprimimos en consola el resultado de la suma
    print("C = ", end='')
    imprimirLista(C)
    print('\n')
    

#! Definicion de la funcion que inicializa los arrays que se sumaran agregando
#! agregando aleatoriamente cada elemento
def inicializarListas(n, bol):

    K = []
    T = []
    #* Para todos los elementos de las listas, tomar en cuenta que 
    #* tienen el mismo tamaño
    for i in range(n):
        #* Agrega aleatoriamente un 0 o 1
        K.append(random.randint(0,1) if bol == 1 else 1)
        T.append(random.randint(0,1) if bol == 1 else 1)

    #* Imprime los valores del array K
    print("K = ", end='')
    imprimirLista(K)
    print('\n')

    #* Imprime los valores del array T
    print("T = ", end='')
    imprimirLista(T)
    print('\n')

    return K, T

#! Definicion de la funcion que realiza la suma binaria entre dos
#! arrays del mismo tamaño
def sumaBinaria(K, T, Z):
    #* Declaracion del array resultado de la suma
    C = []
    #? Declaracion de una variable local que obtendra los ordenes de 
    #? complejidad para cada valor de k
    time = 0

    time += 1
    #* For que funciona como iteracion para cada elemento de los arrays
    for i in range(len(K)): 
        time += 1
        
        #* Sentencia que determina el valor del siguiente elemento a sumar
        C.append(Z ^ K[i] ^ T[i]); time+=1

        #* Sentencia que determina el valor del corrimiento
        Z = (K[i] and Z) or (T[i] and Z) or (K[i] and T[i]); time+=1

    #* Si el ultimo corrimiento es igual a 1, entonces se agrega al array resultado
    if(Z == 1):
        time+=1    
        C.append(Z);time+=1
    
    #? Agregamos el valor actual de t al array global
    totalTime.append(time)
    time = 0
    return C

#! Definicion de la funcion que imprime todos los elementos de una lista
def imprimirLista(lista):
    for item in lista:
        print(item, end='')

#! Definicion de la funcion main 
def main():
    #? Obtengo el archivo donde guardare los tiempos t
    nameFile = "files_practices/pract1.txt" 
    file = open(nameFile, 'w')
    
    #* Para todos los valores de k entre 1 y 10 
    for k in range(10):
        print("Suma binaria con k = ", k + 1)

        #* Realiza la suma binaria
        preSumaBinaria(k+1)
    
    #? Para todos los los tiempos t, los escribe en el archivo
    for item in totalTime:
        #? Sino es el ultimo de la lista, separalo por coma
        if item != totalTime[-1]:
            print(item, file = file , end=', ')
        else:
            print(item, file = file , end='\n')
    

    #? Para todos los los pasos n, los escribe en el archivo
    for item in totalSteps:
        #? Sino es el ultimo de la lista, separalo por coma
        if item != totalSteps[-1]:
            print(item, file = file , end=', ')
        else:
            print(item, file = file , end='\n')

    resultadosAleatorios(file)
    print("aleatorios")
    #? Cierre del archivo donde se escribio
    file.close()

    #*Llamada a la funcion que permitira personalizar las graficas
    personalizarGraficas(nameFile)

def resultadosAleatorios(file):
    x = []
    y = []
    z = []
    totalTime.clear()

    for i in range(1,11):
        n =  2**i
        x,y = inicializarListas(n, 1)
        z = sumaBinaria(x,y,0)

    print(totalTime)
    for item in totalTime:  
        if item != totalTime[-1]:
            print(item, file = file , end=', ')
        else:
            print(item, file = file , end='\n')

#! Definicion de la funcion que permite agregar un titulo y los labels de la grafica
def personalizarGraficas(file):
    #* Determinacion del titulo y los labels de la grafica
    title = "Suma Binaria"
    xlabel = "n : # de pasos donde n = 2^k"
    ylabel = "t : # de iteraciones"

    #* Creamos un objeto de tipo Graphics, mandamos como parametro la ruta completa del archivo
    graphic = Graphics(file)

    #?Llamamos a la funcion que graficara los resultados
    graphic.graficar(title, xlabel, ylabel)

#* Llamada a la funcion main
main()