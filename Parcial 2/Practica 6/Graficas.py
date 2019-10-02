#!/usr/bin/env python
#?ll
import numpy as np
import sys
import matplotlib.pyplot as plt

class Graphics:
    def __init__(self, file):
        self.f = open(file, 'r')
        self.A = self.f.readlines()
        self.n = int(0)
        self.t = int(0)

    def graficar(self, title, xlabel, ylabel, functionLabelO, functionLabelT, functionLabelOm):
        y_aleatorios = self.A[0].split(',')
        x_aleatorios = self.A[1].split(',') 
        y_peores = self.A[2].split(',')
        x_peores = self.A[3].split(',')
        y_mejores = self.A[4].split(',')
        x_mejores = self.A[5].split(',')
        
        for i in range(len(x_peores)):
            x_peores[i] = int(x_peores[i])
            y_peores[i] = int(y_peores[i])
            x_mejores[i] = int(x_mejores[i])
            y_mejores[i] = int(y_mejores[i])
            x_aleatorios[i] = int(x_aleatorios[i])
            y_aleatorios[i] = int(y_aleatorios[i])

        self.n = x_peores[-1]
        self.t = y_peores[-1]

        plt.rc('text', usetex=True)
        plt.rc('font', family='serif', size=11)
        plt.axis([-1, self.n + 1, -1, self.t + 1])
        plt.plot(x_peores,y_peores, "--", label=r"$"+functionLabelO+r"$", lw=1, color="red")
        plt.plot(x_mejores,y_mejores, "--", label=r"$"+functionLabelOm+r"$", lw=1, color="blue")
        plt.scatter(x_aleatorios,y_aleatorios, color='green', label=r"$"+functionLabelT+r"$")


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
