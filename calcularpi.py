#! /usr/bin/python
# -*- coding:utf-8 -*-
#
#
#
#
#
#
# Itsai Mejia
# Sep 22, 2019
# al16760300.AT.ite.DOT.edu.DOT.mx
#

# llamado a liberias
from math import *
from decimal import *
from datetime import datetime
import sys, getopt, argparse

###
##Especificar la cantidad de decimales a ser empleados
getcontext().prec = 2


# Se crea la clase a ser ejecutada
class calcularPI:
    def __init__(self, datos):
        self.datos = datos 
        self.parametro_t = 53 # se define por default
        self.parametro_d = 16
        self.bandera = -1
        try:
            opts, args = getopt.getopt(self.datos, "hn:t:d:f:", ["help","n_val","t_val=", "d_val=", "bandera="])
        except getopt.error:
            print('Modo de ejecutar el codigo:')
            print('calcularpi.py -n [-t <parametro_t> -d <parametro_d> -f <flag>]')
            print('   ')
            print('Escriba solamente calcularpi.py -h para mayor informacion ')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                parser = argparse.ArgumentParser(description='''
                    Programa que permite calcular el valor de PI
                    Se solicita el valor de cuantos numeros 
                    pseudo-aleatorios son con los que desea generar el valor de PI
                    
                    ''', epilog='''

                    ''')
                parser.add_argument('-n', '--n_val', help='Numero de repeticiones', required=True)
                parser.add_argument('-t', '--t_val', help='Parametro para el generador del numero aleatorio',required=False)
                parser.add_argument('-d', '--b_val', help='Parametro para el generador del numero aleatorio',required=False)
                parser.add_argument('-f', '--bandera', help='Parametro para el generador del numero aleatorio',required=False)
                args = parser.parse_args()
            elif opt in ("-n", "--n_val"):
                self.repeticiones = int(arg)
            elif opt in ("-t", "--t_val"):
                self.parametro_t = int(arg)
            elif opt in ("-d", "--d_val"):
                self.parametro_d = int(arg)
            elif opt in ("-f", "--bandera"):
                self.bandera = int(arg)

        # se encarga de definir los parametro necesarios para el generador aleatorio
        self.a = 8 * self.parametro_t + (self.bandera * 3)
        self.m = 2 ** self.parametro_d
        calcularPI.simula(self)

    # se encarga de crear el numero pseudoaleatorio
    def aleatorio(self):
        ahora = datetime.now()
        semilla = ahora.microsecond
        x = (self.a * semilla) % self.m
        rand = Decimal(x) / self.m
        return (rand)

    def simula(self):
        x=0
        for i in range(0,self.repeticiones):
            RND1=calcularPI.aleatorio(self)
            RND2=calcularPI.aleatorio(self)

            evaluar=sqrt(RND1**2+RND2**2)
            x+=1 if evaluar < 1 else 0
        self.valorPI = (4*x) / self.repeticiones

x = calcularPI(sys.argv[1:])

print("El valor de pi es: {0:.4f}".format(x.valorPI))