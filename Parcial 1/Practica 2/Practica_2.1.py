"""
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 2a : "Fibonacci, Recursivo vs. Iterativo"
"""

#*Llamada a las bibliotecas necesarias, en tal caso la biblioteca de graficacion
from Graficas import Graphics

#? Definicion de la variable golbal que ayudara a contar
time = 0

#! Definicion de la funcion main
def main():

	#? Definicion local de la variable global que llevara el conteo de iteraciones
    global time

	#* Recibimos por el shell la cantidad de numeros fibonacci a evaluar
    limit = int(input("Ingresa la cantidad de numeros Fibobacci a encontrar [F(n)] : "))

	#* Abrimos los archivos donde guardaremos los datos recolectados tanto de la funcion recursiva como iterativa
    f1 = open("./files_practices/pract_2.1a.txt", 'w')
    f2 = open("./files_practices/pract_2.1b.txt", 'w')

	#* Para todos los numeros fibonacci entre 1 y lo ingresado desde shell
    for i in range(limit):

		#* Imprimimos el numero de iteracion, el numero fibonacci y el tiempo que total utilizado
		#* y llamamos a la funcion fibonacci recursiva
        print("Iteracion : %d" % int(i + 1))
        fibonacci = fibRecursivo(i)
        print('Numero de la sucecion de fibonacci recursivo: %d' % fibonacci)
        print('Tiempo: %d' % time)

		#? Escribimos en el archivo correspondiente los resultados del tiempo utilizado y
		#? reiniciamos la variable global
        impresion(time, f1, i + 1, limit)
        time = 0

		#* Imprimimos el numero fibonacci y el tiempo que total utilizado
		#* y llamamos a la funcion fibonacci iterativa
        fibonacci = fibIterativo(i)
        print('Numero de la sucecion de fibonacci iterativo: %d' % fibonacci)
        print('Tiempo: %d\n\n' % time)

		#? Escribimos en el archivo correspondiente los resultados del tiempo utilizado y
		#? reiniciamos la variable global
        impresion(time, f2, i + 1, limit)
        time = 0
    
	#* Llamamos a la funcion que escribe el array de numeros fibonacci que sacamos de la evaluacion anterior
    escrituraN(limit, f1)
    escrituraN(limit, f2)

	#* Llamamos funcion que genera valores aleatorios para verificar a que tipo de funcion corresponde
    escribirAlRe(limit, f1)
    escribirAlIt(limit, f2)

	#* Cerramos los archivos donde escribimos los resultados obtenidos
    f1.close()
    f2.close()

	#* Creamos 2 Objetos de tipo graphics para que nos genere 2 graficas
	#* *** Una correspondiente al caso iterativo ***
	#* *** Una correspondiente al caso recursivo ***
    graphicsRe = Graphics("./files_practices/pract_2.1a.txt")
    graphicsIt = Graphics("./files_practices/pract_2.1b.txt")

	#* Graficamos los dos graficas a partir de los resultados obtenidos
    graphicsIt.graficar("Fibonacci Iterativo", "n = n-esimo termino Fibonacci de la sucesion", "t = total de pasos realizados")
    graphicsRe.graficar("Fibonacci Recursivo", "n = n-esimo termino Fibonacci de la sucesion", "t = total de pasos realizados")


#! Definicion de la funcion que genera valores aleatorios dentro de la funcion recursiva
def escribirAlRe(limit, file):
    
	#? Definicion local de la variable global que llevara el conteo de las iteraciones
    global time

	#* Para todos los valores entre 0 y limit
    for i in range(limit):

		#* Llamamos a la funcion que calculara el i-esimo termino fibonacci recursivamente
        fibRecursivo(i)

		#* Escribimos en fila recibido los resultados del tiempo usado
        impresion(time, file, i + 1, limit)

		#? Reiniciamos el contador global
        time = 0

#! Definicion de la funcion que genera valores aleatorios dentro de la funcion iterativo
def escribirAlIt(limit, file):
    
    #? Definicion local de la variable global que llevara el conteo de las iteraciones
    global time

	#* Para todos los valores entre 0 y limit
    for i in range(limit):

		#* Llamamos a la funcion que calculara el i-esimo termino fibonacci iterativamente
        fibIterativo(i)

		#* Escribimos en fila recibido los resultados del tiempo usado
        impresion(time, file, i + 1, limit)

		#? Reiniciamos el contador global
        time = 0

#! Definicion de la funcion que imprime los n terminos fibonacci usados en el archivo recivido
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

#! Definicion de la funcion fibonacci recursiva
def fibRecursivo(n):
	#? Definicion local de la variable global que llevara el conteo total de iteraciones
    global time

	#? Incrementamos 1 a time
    time += 1

	#* Si n = 0  o n = 1
    if n == 0 or n == 1:
		#? Incrementa en 1 a time y retorna 1
        time += 1
        return 1
	#? Incrementamos 1 a time

	#? Retorna Fibonacci(n-1) + Fibonacci(n-2)
    return fibRecursivo(n-1) + fibRecursivo(n-2)

#! Definicion de la funcion fibonacci iterativa
def fibIterativo(n):
    #? Definicion local de la variable global que llevara el conteo total de iteraciones
    global time

	#* Definicion de las variables auxiliares que acumularan los resultados del n-esimo termino + (n-1)-termino fibonacci
    a=1;time += 1 
    b=1;time += 1

    time += 1
	#* Para todos los valores terminos fibonacci  desde 1 hasta n
    for i in range(1, n, 1):
		#* Asignar a = b y b = a + b
        a,b = b,a+b ;time += 1
	
	#* Retonar el valor de b
    time += 1
    return b

#* Llama a la funcion main()
if __name__ == "__main__":
    main()

