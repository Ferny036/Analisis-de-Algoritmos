#!/usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt

class Graphics:
    def __init__(self, file):
        self.f = open(file, 'r')
        self.A = self.f.readlines()
        self.n = int(0)
        self.t = int(0)

    def graficar(self, title, xlabel, ylabel):
        x = self.A[1].split(',')
        y = self.A[0].split(',')
        aleatorios = self.A[2].split(',')
        
        for i in range(len(x)):
            x[i] = int(x[i])
            y[i] = int(y[i])
            aleatorios[i] = int(aleatorios[i])

        self.n = x[-1]
        self.t = y[-1]

        plt.axis([-30, self.n + 100, 0, self.t + 1])
        plt.plot(x,y, color="red", label="O(g(n)) aprox.")
        plt.scatter(x,aleatorios, color="green", label="Random points")
        plt.scatter(x,y, color="blue", label="O(g(n)) real")

        plt.legend(loc="upper left")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


        plt.show()

if(len(sys.argv) > 1):
    title = sys.argv[2]
    xlabel = sys.argv[3]
    ylabel = sys.argv[4]
    graphic = Graphics(sys.argv[1])
    graphic.graficar(title, xlabel, ylabel)
