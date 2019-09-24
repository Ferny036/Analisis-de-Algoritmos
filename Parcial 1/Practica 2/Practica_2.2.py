"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 2b : "Suma  de los primeros n numero cubos"
""" 
#*Llamada a las bibliotecas necesarias, en tal caso la biblioteca de graficacion
from Graficas import Graphics
import sys

#? Definicion de las variables globales a utilizar para el conteo de las iteraciones
time = 0
totalTime = []

#! Definicion de la funcion que permite producir resultador aleatorios apartir de la funcion normal
def escribirAlIt(limit, file):
    #? Definicion local de la variable global que contara el total de iteraciones
    global time

	#* Para todo el rango entre 0 y limit
    for i in range(limit):
		#* Llamar a la funcion iterativa de suma de n numeros cubicos
        SIt(i + 1)

		#* Se escribe en el archivo correspondiente
        impresion(time, file, i + 1, limit)

		#? Reiniciamos el contador global
        time = 0

#! Definicion de la funcion que imprime la suma de los n numeros cubicos usados en el archivo recibido
def escrituraN(n, file):

	#* Para todos los valores de 1 hasta n, imprimelos en sucesion
    for i in range(n):
        impresion(i + 1, file, i + 1, n)
    
#! Definicion de la funcion que determina el modo de impresion para los resultado recibidos
def impresion(time, file, index, limit):

	#* Si index es el ultimo elemento (limit) escribe un salto de linea
    if index == limit:
        print(time, file = file, end='\n')
	#* Sino escribe una comida seguida de un espacio
    else: 
        print(time, file = file, end=', ')

#! Definicion de la funcion recursiva de la suma de los n numero cubicos
def SRe(n):

	#? Definicion local de la variable global
    global time
    time += 1

	#* Si n es igual al caso base retorna 1
    if n == 1:
        time += 1
        return 1
	#* Sino retorna el valor de S(n-1) + n^3
    else:
        time += 2
        return SRe(n-1) + (n**3)

#! Definicion de la funcion iterativa de la suma de los n numeros cubicos
def SIt(n):
	#? Definicion local de la variable global
    global time

	#* Definicion de la variable local que llevara lo acumulado
    acum = 0 ; time += 1
    time += 1

	#* Para todos los valores entre 0 y n
    for i in range(n):
        time += 1
		#* Acumula con la suma de lo obtenido antes mas i^3
        acum = acum + ((i + 1) ** 3)

    time += 1

	#* Retorna lo acumulado
    return acum

#! Definicion de la funcion main
def main():

	#? Definicion local de la variable global que contara el total de iteraciones
	global time

	#* Abrimos los archivos correspondientes sonde se escribiran los resultados obtenidos de time
	f1 = open("./files_practices/pract_2.2a.txt", 'w')
	f2 = open("./files_practices/pract_2.2b.txt", 'w')

	#* Obtenenmos desde shell un valor maximo entero a calcular
	num = int(input("Ingrese un numero entero positivo maximo a calcular: "))

	#* Para todos los valores desde 0 hasta el valor recibido desde shell
	for i in range(num):

		#* Llama a la funcion que calculara la suma de los primeros n numeros cubicos recursivamente
		print("Iteracion n : %d" % i)
		print("La suma de los primeros %d numeros cubicos recursivamente: %d\n" % (i, SRe(i + 1)))

		#? Ingreso los valores obtenidos en la lista global
		totalTime.append(time)

		#* Escribe en el archivo correspondiente los resultados obtenidos
		impresion(time, f1, i + 1, num)

		#? Reiniciamos el contador global
		time = 0

		#* Llama a la funcion que calculara la suma de los primeros n numeros cubicos iterativamente
		SIt(i + 1)

		#* Escribe en el archivo correspondiente los resultados obtenidos
		impresion(time, f2, i + 1, num)
		
		#? Reiniciamos el contador global
		time = 0
    
	#* Llama a la funcion que escribe en el archivo correspondiente los valores treabajados
	escrituraN(num, f1)
	escrituraN(num, f2)

	#* Lama a la funcion que determina escribe en el archivo correspondiente los resultados de las iteraciones
	escribirAlIt(num, f2)
	for i in range(num):
		impresion(totalTime[i], f1, i + 1, num)

	#* Cierra los archivos usados
	f1.close()
	f2.close()

	#* Creamos dos objetos del tipo graphics para graficar nuestros resultados
	graphicsRe = Graphics("./files_practices/pract_2.2a.txt")
	graphicsIt = Graphics("./files_practices/pract_2.2b.txt")

	#* Graficamos los resultados obtenidos
	graphicsIt.graficar("Suma de numeros cubicos Iterativo", "n = n-esimo termino de la suma", "t = total de pasos realizados")
	graphicsRe.graficar("Suma de numeros cubicos Recursivo", "n = n-esimo termino de la suma", "t = total de pasos realizados")



if __name__ == "__main__":
    main()