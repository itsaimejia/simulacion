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
from datetime import *
import sys, getopt, argparse

###
##Especificar la cantidad de decimales a ser empleados
getcontext().prec = 2


# Se crea la clase a ser ejecutada
class supermercado:
    def __init__(self, datos):
        self.datos = datos
        self.parametro_t = 264  # se define por default
        self.parametro_d = 22
        self.bandera = 1
        try:
            opts, args = getopt.getopt(self.datos, "hp:t:d:f:", ["help", "p_val", "t_val=", "d_val=", "bandera="])
        except getopt.error:
            print('Modo de ejecutar el codigo:')
            print('calcularpi.py -p <cantidad_personas> [-t <parametro_t> -d <parametro_d> -f <flag>]')
            print('   ')
            print('Escriba solamente calcularpi.py -h para mayor informacion ')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                parser = argparse.ArgumentParser(description='''
                El programa permite determinar la mejor opcion de cuantas personas 
                es mejor para la empresa emplear
                Solo contamos con 4 grupos (numero de empleados) con los que evaluaremos 
                El programa pide -p y este puede tomar valores 
                3 o 4 o 5 o 6
                    ''', epilog='''

                    ''')
                parser.add_argument('-p', '--p_val', help='Numero de personas a evaluar', required=True)
                parser.add_argument('-t', '--t_val', help='Parametro para el generador del numero aleatorio',
                                    required=False)
                parser.add_argument('-d', '--b_val', help='Parametro para el generador del numero aleatorio',
                                    required=False)
                parser.add_argument('-f', '--bandera', help='Parametro para el generador del numero aleatorio',
                                    required=False)
                args = parser.parse_args()
            elif opt in ("-p", "--p_val"):
                self.personas = int(arg)
            elif opt in ("-t", "--t_val"):
                self.parametro_t = int(arg)
            elif opt in ("-d", "--d_val"):
                self.parametro_d = int(arg)
            elif opt in ("-f", "--bandera"):
                self.bandera = int(arg)

        # se encarga de definir los parametro necesarios para el generador aleatorio
        self.a = 8 * self.parametro_t + (self.bandera * 3)
        self.m = 2 ** self.parametro_d

        supermercado.simula(self)

    # se encarga de crear el numero pseudoaleatorio
    def aleatorio(self):
        ahora = datetime.now()
        semilla = ahora.microsecond
        x = (self.a * semilla) % self.m
        rand = Decimal(x) / self.m
        return (rand)

    def tiempoLlegadas(self):
        # tiempo entre llegadas

        rnd = supermercado.aleatorio(self)
        return (20 if rnd <= 0.02 else 25 if rnd <= 0.10 else
                30 if rnd <= 0.22 else 35 if rnd <= 0.47 else
                40 if rnd <= 0.67 else 45 if rnd <= 0.82 else
                50 if rnd <= 0.92 else 55 if rnd <= 0.97 else 60 )


    def llegadaCamiones(self):
        # cuantos camiones llegaron
        rnd = supermercado.aleatorio(self)
        return(
            0 if rnd <= 0.50 else
            1 if rnd <= 0.75 else
            2 if rnd <= 0.90 else
            3
        )
    def simula(self):
        #valores definidos en general para cada caso
        min_llegadas = supermercado.tiempoLlegadas(self)
        camiones = supermercado.llegadaCamiones(self)
        inicioServicio= timedelta(hours=11,minutes=00)

        while(camiones > 0):
            if 3 <= self.personas <= 6:
                if self.personas == 3:
                    rnd = supermercado.aleatorio(self)
                    tiempoServicio = (
                    )
                elif self.personas == 4:
                    rnd = supermercado.aleatorio(self)
                    tiempoServicio = (
                    )
                elif self.personas == 5:
                    rnd = supermercado.aleatorio(self)
                    tiempoServicio = (
                    )
                elif self.personas == 6:
                    rnd = supermercado.aleatorio(self)
                    tiempoServicio = (
                    )
            else:
                print("Numero no valido")


x = supermercado(sys.argv[1:])

