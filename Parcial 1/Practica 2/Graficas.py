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

        plt.rc('text', usetex=True)
        plt.rc('font', family='serif', size=11)
        plt.axis([-1, self.n + 1, -1, self.t + 1])
        plt.plot(x,y, color="red", label=r"$\theta$(g(n)) aprox.")
        plt.scatter(x,aleatorios, color="blue", label="Random points")

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
