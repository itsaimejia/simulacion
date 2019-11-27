#! /usr/bin/python
# -*- coding:utf-8 -*-
#
#
# 
#
#
#
# Itsai Zempoaltecatl Mejia
# Jose Carlos Munoz Ramirez
# Nov 27, 2019
# al16760300.AT.ite.DOT.edu.DOT.mx(Itsai)
# al15201330.AT.ite.DOT.edu.DOT.mx(Jose Carlos)
#

# llamado a liberias
from decimal import *
import random
import math
import sys, getopt, argparse
import numpy as np

# Especificar la cantidad de decimales a ser empleados
getcontext().prec = 2

# Se crea la clase a ser ejecutada
class maquinas:
    def __init__(self, datos):
        self.datos = datos
        self.semilla=2359
        self.m=66251
        self.a=523
        try:
            opts, args = getopt.getopt(self.datos, "hs:x:m:a:",["help", "semanas=","semilla=","valor_m=","valor_a="])
        except getopt.error:
            print('Modo de ejecutar el codigo:')
            print('proyecto.py -s <semanas> [-x <semilla> -m <valor_m> -a <valor_a>]')
            print('   ')
            print('Escriba solamente proyecto.py -h para mayor informacion ')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                parser = argparse.ArgumentParser(description='''
                    descripcion
					''', epilog='''
                    epilogo
					''')
                parser.add_argument('-s', '--semanas', help='Semanas que se evaluaran',
                                    required=True)
                parser.add_argument('-p', '--productos', help='Cantidad de productos vendidos',
                                    required=True)
                parser.add_argument('-x', '--semilla', help='Parametro para el generador del numero aleatorio',
                                    required=False)
                parser.add_argument('-m', '--m', help='Parametro para el generador del numero aleatorio',
                                    required=False)
                parser.add_argument('-a', '--a', help='Parametro para el generador del numero aleatorio',
                                    required=False)
                args = parser.parse_args()
            elif opt in ("-s", "--semanas"):
                self.semanas = int(arg)
            elif opt in ("-p", "--productos"):
                self.productos = int(arg)
            elif opt in ("-x", "--x"):
                self.semilla = int(arg)
            elif opt in ("-m", "--m"):
                self.m = int(arg)
            elif opt in ("-a", "--a"):
                self.a = int(arg)

        maquinas.simula(self)

    #def maquina1(self):

    #def maquina2(self):

    def maquina3(self):
        xn=self.semilla
        intervalo=0
        ganancia=0
        for i in range(0,220):
            xi = (self.a * xn) % self.m
            xn=xi
            rnd = xi/ self.m
            vRND=abs((1/2.32)*(np.log(rnd)))

            if vRND <= 0.46:
                intervalo=random.uniform(8,12.6)
            elif vRND <= 0.75:
                intervalo=random.uniform(12.7,17.3)
            elif vRND <= 0.86: 
                intervalo=random.uniform(17.4,22)
            elif vRND <= 0.94:
                intervalo=random.uniform(22.1,26.7)
            elif vRND <= 1:
                intervalo= random.uniform(26.8,31.4)
            
            ganancia+=intervalo

        return ganancia

    def simula(self):
        gMaquina3=0
        for x in range(0,self.semanas):
            gMaquina3+=maquinas.maquina3(self)

        self.maquina3porSemana=gMaquina3/self.semanas
        self.maquina3porMes=gMaquina3/12



x = maquinas(sys.argv[1:])

print("La ganancia de la maquina 3 por semana es de: {}".format(x.maquina3porSemana))
print("La ganancia de la maquina 3 por mes es de: {}".format(x.maquina3porMes))

