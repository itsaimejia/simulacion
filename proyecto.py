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
import random
import math
import sys, getopt, argparse

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
                    El programa permite determinar un aproximado de las ganancias totales
		    por semanas, y en caso de ser multiplos de 52 dara un aproximado de las
		    ganacias mensuales. Las ganancis de las maquinas estan determinadas base
		    a las observaciones que se hicieron sobre las cantidades compradas de los
		    alumnos a traves de un determinado tiempo.
					''', epilog='''
                    El resultado estara en terminos de promedios semanales y mensuales.
					''')
                parser.add_argument('-s', '--semanas', help='Semanas que se evaluaran',
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
            elif opt in ("-x", "--x"):
                self.semilla = int(arg)
            elif opt in ("-m", "--m"):
                self.m = int(arg)
            elif opt in ("-a", "--a"):
                self.a = int(arg)

        maquinas.simula(self)

    def maquina1(self):
        xn=self.semilla
        intervalo=0
        ganancia=0
        for i in range(0,45):
            xi = (self.a * xn) % self.m
            xn=xi
            rnd = xi/ self.m
            vRND=abs((1/2.32)*(math.log(rnd)))

            if vRND <= 0.46:
                intervalo=random.uniform(8,13.6)
            elif vRND <= 0.75:
                intervalo=random.uniform(13.7,19.3)
            elif vRND <= 0.86: 
                intervalo=random.uniform(15.4,25)
            elif vRND <= 0.94:
                intervalo=random.uniform(25.1,30.7)
            elif vRND <= 1:
                intervalo= random.uniform(30.8,36.4)
            
            ganancia+=intervalo

        return ganancia

    def maquina3(self):
        xn=self.semilla
        intervalo=0
        ganancia=0
        for i in range(0,220):
            xi = (self.a * xn) % self.m
            xn=xi
            rnd = xi/ self.m
            vRND=abs((1/2.32)*(math.log(rnd)))

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

    def maquina4(self):
        xn=self.semilla
        intervalo=0
        ganancia=0
        for i in range(0,136):
            xi = (self.a * xn) % self.m
            xn=xi
            rnd = xi/ self.m
            vRND=abs((1/2.32)*(math.log(rnd)))

            if vRND <= 0.514705882:
                intervalo=random.uniform(8,13)
            elif vRND <= 0.75735294:
                intervalo=random.uniform(13.1,18.1)
            elif vRND <= 0.83823529: 
                intervalo=random.uniform(18.2,23.2)
            elif vRND <= 0.94117647:
                intervalo=random.uniform(23.3,28.3)
            elif vRND <= 1:
                intervalo= random.uniform(28.4,33.4)
            
            ganancia+=intervalo

        return ganancia


    def simula(self):
        gMaquina1=0
        gMaquina3=0
        gMaquina4=0
        for x in range(0,self.semanas):
            gMaquina1+=maquinas.maquina1(self)
            gMaquina3+=maquinas.maquina3(self)
            gMaquina4+=maquinas.maquina4(self)

        self.maquina1porSemana=gMaquina1/self.semanas
        self.maquina1porMes=gMaquina1/12

        self.maquina3porSemana=gMaquina3/self.semanas
        self.maquina3porMes=gMaquina3/12

        self.maquina4porSemana=gMaquina4/self.semanas
        self.maquina4porMes=gMaquina4/12



x = maquinas(sys.argv[1:])
print("La ganancia de la maquina 1 por semana es de: {0:.2f}".format(x.maquina1porSemana))
print("La ganancia de la maquina 1 por mes es de: {0:.2f}\n".format(x.maquina1porMes))

print("La ganancia de la maquina 3 por semana es de: {0:.2f}".format(x.maquina3porSemana))
print("La ganancia de la maquina 3 por mes es de: {0:.2f}\n".format(x.maquina3porMes))

print("La ganancia de la maquina 4 por semana es de: {0:.2f}".format(x.maquina4porSemana))
print("La ganancia de la maquina 4 por mes es de: {0:.2f}\n".format(x.maquina4porMes))
