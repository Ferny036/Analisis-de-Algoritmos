/*
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
Grupo: 3CV2
Semestre: 20/1

Integrantes:
Rivera Paredes Fernando Daniel
Contreras Paredes Alejandro

Practica 1b : Algortmo de Euclides (MCD)
*/
//* Llamada a bibliotecas externas para uso de impresion y  calculos matematicos 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//? Definicion de la variable global que registrara la complejidad
unsigned long long int t = 0;

//! Definicion de la funcion de Euclides para calcular el MCD de 2 numero enteros iterativamente
int Euclides(unsigned long long int m, unsigned long long int n){
    //? Creamos la variable r como auxiliar
    unsigned long long int r = 0; t++;

    t++;
    //? Mientras n sea distinto de 0 en todas las operaciones de modulo
    while (n != 0){
        //? Se desarrolla el algoritmo de Euclides
        r = m % n;t++;
        m = n;t++;
        n = r;t++;
    }

    t++;
    //? Retornamos el MCD de m y n
    return m;
}

//! Definicion de la funcion que nos permite calcular potencias de 10
unsigned long long int potencia(unsigned long long int x, unsigned long long int i){
    //* El parametro recivido se elveva a la potencia deseada y lo retornamos
    x = pow(10,i);
    return x;
}

//! Definicion de la funcion que nos permite obtener los ultimos 2 numeros en la serie 
//! Fibonacci con la misma cantidad de digitos
unsigned long long int *Fibonnacci(int n){

    //* Declaracion de las variables auxiliares para encontrar los elementos Fibonacci solicitados
    unsigned long long int c = 0;
    unsigned long long int sig = 1, aux = 0, a = 1, j = 0, x = 0;

    //* Declaracion del arreglo que almacenara todos los elementos Fibonacci solicitados
    unsigned long long int *A = (unsigned long long int*)malloc(20*sizeof(unsigned long long int));

    //* Mientras i tenga menos o 'n' digitos
    for (int i = 0; i <= n; i++){
        
        //* Elevamos x una potencia de 10 mas
        x = potencia(10,i);

        //* Mientras x sea mayor que el resultado de la ultima suma de Fibonacci 
        while(x > sig) {
            //* Jugamos con las variables auxiliares para no perder valores anteriores
            c = A[j];
            a = sig;

            //* Realizamos las sumas de los 2 numeros anteriores de fibonacci
            sig = aux + sig;
            aux = a;

            //* Los almacenamos temporalmente en el arreglo
            A[j] = aux;
            A[j+1] = sig;
        }

        //* Asignamos los valores de c & a (que actualmente contienen los ultimos 2 numeros con la misma 
        //* cantidad de digitos) en el arreglo de numeros Fibonacci
        A[j] = c;
        A[j+1] = a;

        //* Incrementamos j en 2 para desplazarnos 2 espacios a la derecha
        j += 2;
    }

    //* Retornamos el arreglo a utilizar posteriormente
    return A;
}

//! Definicion de la funcion main encargada de obtener los valores de t
int main(int argc, char const *argv[]){
    
    //? Definimos el archivo donde escribiremos los resultados de t
    FILE *file;
    file = fopen(argv[1], "w");

    //* Determinamos el limite de digitos que tendra la lista de numeros a evaluar ([2n - 2] * 2)
    int limit = 38;

    //* Definicion del index auxiliar para impresion
    int i = 0;

    //* Definicion del arreglo que almacenara los pares de numeros fibonacci deseados
    unsigned long long int *array = (unsigned long long int *)malloc(sizeof(unsigned long long int)*20);
    
    //* Apunta a la direccion que devuelve la funcion Fibonacci
    array = Fibonnacci(limit);

    //* Realizamos una pre impresion para ver una tabla de valores
    printf("%s\t\t%s\t\t%s\n", "Valores de M", "Valores de N", " Valores t");

    //* Para todos los pares del array
    for (i = 0; i <= limit; i+=2){

        //* Realizamos el calculo del MCD por pares
        Euclides(array[i], array[i + 1]);

        //* Imprimimos su valor 
        printf("%llu\t\t\t%llu\t\t\t", array[i], array[i + 1]);
        printf("%llu\n", t);

        //? Condicion de impresion para que el ultimo elemento se imprima en el archivo
        //? el ultimo elemento sin ',', sobre todos los valores de t
        if(i != limit){
            fprintf(file, "%llu, ", t);
        }else{
            fprintf(file, "%llu\n", t);
        }
        t=0;
            
    }

    for(i = 0; i<=limit; i+=2){
        if(i != limit){
            fprintf(file, "%llu, ", array[i+1]);
        }else{
            fprintf(file, "%llu\n", array[i+1]);
        }
    }
    
    //* Liberamos el espacio de memoria del array utilizado y cerramos el archivo donde escribimos
    free(array);
    fclose(file);
    
    return 0;
}

