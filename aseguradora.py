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
from decimal import *
from datetime import datetime
import sys, getopt, argparse

###
##Especificar la cantidad de decimales a ser empleados
getcontext().prec = 2


# Se crea la clase a ser ejecutada
class accidentes:
    def __init__(self, datos):
        self.datos = datos
        self.filas = 50  # se define por default
        self.columnas = 10
        try:
            opts, args = getopt.getopt(self.datos, "ht:d:b:n:m:",
                                       ["help", "t_val=", "d_val=", "bandera=", "filas=", "columnas="])
        except getopt.error:
            print('Modo de ejecutar el codigo:')
            print('aseguradora.py -t <parametro_t> -d <parametro_d> -b <flag> [-n <filas> -m <columnas>]')
            print('   ')
            print('Escriba solamente aseguradora.py -h para mayor informacion ')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                parser = argparse.ArgumentParser(description='''
					El programa permite conocel el monto, la probabilidad y la cantidad 
					de cuanto pagara la aseguradora en caso de ocurrir un accidente
					''', epilog='''
					El resultado estara en terminos del promedio del numero de accidentes (y monto) que 
					la aseguradora tuvo que pagar

					''')
                parser.add_argument('-t', '--t_val', help='Parametro para el generador del numero aleatorio',
                                    required=True)
                parser.add_argument('-d', '--b_val', help='Parametro para el generador del numero aleatorio',
                                    required=True)
                parser.add_argument('-b', '--bandera', help='Parametro para el generador del numero aleatorio',
                                    required=True)
                parser.add_argument('-n', '--filas', help='Numero de repeticiones fila', required=False)
                parser.add_argument('-m', '--columnas', help='Numero de repeticiones columna', required=False)
                args = parser.parse_args()
            elif opt in ("-t", "--t_val"):
                self.parametro_t = int(arg)
            elif opt in ("-d", "--d_val"):
                self.parametro_d = int(arg)
            elif opt in ("-b", "--bandera"):
                self.bandera = int(arg)
            elif opt in ("-n", "--fila"):
                self.filas = int(arg)
            elif opt in ("-m", "--columna"):
                self.columnas = int(arg)

        # se encarga de definir los parametro necesarios para el generador aleatorio
        self.a = 8 * self.parametro_t + (self.bandera * 3)
        self.m = 2 ** self.parametro_d

        accidentes.simula(self)

    # se encarga de crear el numero pseudoaleatorio
    def aleatorio(self):
        ahora = datetime.now()
        semilla = ahora.microsecond
        x = (self.a * semilla) % self.m
        rand = Decimal(x) / self.m
        return (rand)

    def simula(self):
        pagos = 0
        promedios = []
        dic_pagos = {
            "500": 0,
            "1000": 0,
            "2000": 0,
            "5000": 0
        }
        for i in range(0, self.columnas):
            montos = []
            for j in range(0, self.filas):
                valor = accidentes.aleatorio(self)
                if valor <= 0.60:
                    monto = 0
                    pagos += 0
                elif valor <= 0.80:
                    monto = 500
                    pagos += 1
                    dic_pagos["500"] = int(dic_pagos.get("500")) + 1
                elif valor <= 0.90:
                    monto = 1000
                    pagos += 1
                    dic_pagos["1000"] = int(dic_pagos.get("1000")) + 1
                elif valor <= 0.95:
                    monto = 2000
                    pagos += 1
                    dic_pagos["2000"] = int(dic_pagos.get("2000")) + 1
                elif valor <= 1.0:
                    monto = 5000
                    pagos += 1
                    dic_pagos["5000"] = int(dic_pagos.get("5000")) + 1
                montos.append(monto)
            promedios.append(sum(montos) / len(montos))


        self.pagoPromedio = sum(promedios) / self.columnas
        self.pagos = pagos
        self.probabilidad = ((Decimal(pagos) / (self.filas * self.columnas))) * 100
        self.cPagos = dic_pagos


x = accidentes(sys.argv[1:])

total = x.filas * x.columnas
print("Se pago en " + repr(x.pagos) + " ocaciones de " + repr(
    total) + ", lo que significa que la probabilidad de pagar es {0:.2f}".format(x.probabilidad) + "%")
print("El pago promedio es: {0:.2f}".format(x.pagoPromedio))
print(x.cPagos)
