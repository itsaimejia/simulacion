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
import random 



#Se crea la clase a ser ejecutada
class empresa: 
	def __init__(self, datos):
		self.datos=datos
		self.semilla=9577
		self.t=25
		self.bandera=1
		self.d=23
		try:
			opts,args=getopt.getopt(self.datos,"hA:",["help","anios="])
		except getopt.error:
			print ('Modo de ejecutar el codigo:')
			print ('CalcularCamiones.py -A <anios> ')
			print ('   ')
			print ('Escriba solamente CalcularCamiones.py -h para mayor informacion ')
			sys.exit(2)
		for opt,arg in opts:
			if opt in ("-h","--help"):
				parser=argparse.ArgumentParser(description='''
					El programa permite determinar la cantidad optima de camiones que la empresa debe 
					adquirir para poder transportar la mercancia desde el area de produccion hasta
					el almacen. Se hace el calculo por anios, el usuario ingresa cuantos anios desea
					calcular
					Se utiliza el metodo de generacion de pseudonumeros aleatorios para el calculo
					''', epilog='''
					Al termino de la ejecucion el programa proporciona la cantidad de los camiones
					optimos que la empresa debe adquirir
					''')
				parser.add_argument('-A','--anios', help='Anios a evaluar', required=True)
				args=parser.parse_args()
			elif opt in ("-A","--anios"):
				self.anios=int(arg)

		self.a=8*self.t+(self.bandera*3)
		self.m=2**self.d

		empresa.calcula(self)

	def produccion(rnd):
		return ( 
			random.uniform(50,55) if rnd <=0.10 else
			random.uniform(55,60) if rnd <=0.25 else
			random.uniform(60,65) if rnd <=0.55 else
			random.uniform(65,75) if rnd <=0.90 else
			random.uniform(75,80) if rnd <=0.98 else
			random.uniform(80,85)
			)
	def capacidad(rnd):
		return (
			random.uniform(4,4.5) if rnd <= 0.30 else
			random.uniform(4.5,5) if rnd <= 0.70 else
			random.uniform(5,5.5) if rnd <= 0.90 else
			random.uniform(5.5,6)
			)
		
	def calcula(self):
		camiones=[]
		xn=self.semilla
		produccionExtra=0
		for i in range(0,self.anios):
			for i in range(0,250):
				xi=(self.a*xn)%self.m
				xn=xi
				rnd=Decimal(xi)/self.m
				camiones.append(empresa.produccion(rnd)//empresa.capacidad(rnd))
				produccionExtra+=1 if empresa.produccion(rnd)%empresa.capacidad(rnd)>1 else 0
		camionesExtra=((produccionExtra/self.anios)*100)//100000
		self.camionesOptimos=(sum(camiones)//len(camiones))+camionesExtra


x=empresa(sys.argv[1:])
print("En base a la prueba de {} anios la cantidad optima de camiones que debe adquirir la empresa es de: {}".format(x.anios,x.camionesOptimos))