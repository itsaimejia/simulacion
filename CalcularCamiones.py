#! /usr/bin/python
#-*- coding:utf-8 -*-
#
#Calculo de los camiones optimos que necesita una empresa
#adquirir para poder solventar la necesidad de 
#transporte de su produccion a un almacen situado a 30 km
#
#
#Itsai Mejia
#Nov 07, 2019
#al16760300.AT.ite.DOT.edu.DOT.mx
#

#llamado a liberias
from decimal import *
import sys, getopt, argparse




#Se crea la clase a ser ejecutada
class empresa: 
	def __init__(self, datos):
		self.datos=datos
		self.semilla=9577
		self.t=25
		self.bandera=1
		self.d=23
		try:
			opts,args=getopt.getopt(self.datos,"hD:",["help","dias="])
		except getopt.error:
			print ('Modo de ejecutar el codigo:')
			print ('CalcularCamiones.py -D <dias> ')
			print ('   ')
			print ('Escriba solamente CalcularCamiones.py -h para mayor informacion ')
			sys.exit(2)
		for opt,arg in opts:
			if opt in ("-h","--help"):
				parser=argparse.ArgumentParser(description='''
					El programa permite determinar la cantidad optima de camiones que la empresa debe 
					adquirir para poder transportar la mercancia desde el area de produccion hasta
					el almacen. El calculo se estima en base a los dias que la empresa trabaja en el anio
					ya que son los camiones que se necesitaran en este lapso 
					Se utiliza el metodo de generacion de pseudonumeros aleatorios para el calculo
					''', epilog='''
					Al termino de la ejecucion el programa proporciona la cantidad de los camiones
					optimos que la empresa debe adquirir
					''')
				parser.add_argument('-D','--dias', help='Dias del anio que la empresa trabaja', required=True)
				args=parser.parse_args()
			elif opt in ("-D","--dias"):
				self.dias=int(arg)

		self.a=8*self.t+(self.bandera*3)
		self.m=2**self.d

		empresa.calcula(self)

	def produccion(random):
		return ( 
			(50+55)/2 if random <=0.10 else
			(55+60)/2 if random <=0.25 else
			(60+65)/2 if random <=0.55 else
			(65+75)/2 if random <=0.90 else
			(75+80)/2 if random <=0.98 else
			(80+85)/2
			)
	def capacidad(random):
		return (
			(4+4.5)/2 if random <= 0.30 else
			(4.5+5)/2 if random <= 0.70 else
			(5+5.5)/2 if random <= 0.90 else
			(5.5+6)/2
			)
		
	def calcula(self):
		camiones=[]
		xn=self.semilla

		for i in range(0,self.dias):
			xi=(self.a*xn)%self.m
			xn=xi
			random=Decimal(xi)/self.m
			camiones.append(empresa.produccion(random)//empresa.capacidad(random))
		self.camionesOptimos=sum(camiones)//self.dias


x=empresa(sys.argv[1:])
print("Camiones optimos que debe adquirir la empresa: {}".format(x.camionesOptimos))