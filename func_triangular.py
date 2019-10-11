#! /usr/bin/python
#-*- coding:utf-8 -*-
#
#
# 
#
#
#
#Itsai Mejia
#Oct 7, 2019
#al16760300.AT.ite.DOT.edu.DOT.mx
#

#llamado a liberias
from math import *
from decimal import *
from datetime import datetime
import sys, getopt, argparse
###
##Especificar la cantidad de decimales a ser empleados
getcontext().prec=2
#Se crea la clase a ser ejecutada
class tinas: 
	def __init__(self, datos):
		self.datos=datos
		self.filas=5 #se define por default 
		self.columnas=24000
		self.parametro_t=30
		self.parametro_d=10
		self.bandera=1
		try:
			opts,args=getopt.getopt(self.datos,"hA:C:B:t:d:f:n:m:",["help","A_val","C_val","B_val","t_val=","d_val=","bandera=","filas=","columnas="])
		except getopt.error:
			print ('Modo de ejecutar el codigo:')
			print ('func_triangular.py -A <valor_a> -C <valor_C> -B <valor_B> [-t <parametro_t> -d <parametro_d> -f <flag> -n <filas> -m <columnas>]')
			print ('   ')
			print ('Escriba solamente func_triangular.py -h para mayor informacion ')
			sys.exit(2)
		for opt,arg in opts:
			if opt in ("-h","--help"):
				parser=argparse.ArgumentParser(description='''
					''', epilog='''
					aaaaaaaaaa
					''')
				parser.add_argument('-A', '--A_val', help='Valor de A', required=True)
				parser.add_argument('-C', '--C_val', help='Valor de C', required=True)
				parser.add_argument('-B', '--B_val', help='Valor de B', required=True)
				parser.add_argument('-t','--t_val', help='Parametro para el generador del numero aleatorio', required=False)
				parser.add_argument('-d','--b_val', help='Parametro para el generador del numero aleatorio', required=False)
				parser.add_argument('-f','--bandera', help='Parametro para el generador del numero aleatorio', required=False)
				parser.add_argument('-n','--filas', help='Numero de repeticiones fila', required=False)
				parser.add_argument('-m','--columnas', help='Numero de repeticiones columna', required=False)

				args=parser.parse_args()
			elif opt in ("-A", "--A_val"):
				self.valor_a=int(arg)
			elif opt in ("-C", "--C_val"):
				self.valor_c=int(arg)
			elif opt in ("-B", "--B_val"):
				self.valor_b=int(arg)
			elif opt in ("-t","--t_val"):
				self.parametro_t=int(arg)
			elif opt in ("-d","--d_val"):
				self.parametro_d=int(arg) 
			elif opt in ("-f","--bandera"):
				self.bandera=int(arg)
			elif opt in ("-n","--fila"):
				self.filas=int(arg)
			elif opt in ("-m","--columna"):
				self.columnas=int(arg)


		#se encarga de definir los parametro necesarios para el generador aleatorio
		self.a= 8*self.parametro_t+(self.bandera*3)
		self.m= 2**self.parametro_d

		self.k1=(self.valor_b-self.valor_a)*(self.valor_c-self.valor_a)
		self.k3=(self.valor_b-self.valor_a)*(self.valor_b-self.valor_c)


		tinas.simula(self)

	#se encarga de crear el numero pseudoaleatorio
	def aleatorio(self):
		ahora=datetime.now()
		semilla=ahora.microsecond
		x=(self.a*semilla)%self.m
		rand=Decimal(x)/self.m
		return (rand)

	def simula(self):

		contador=0
		for i in range(0,self.columnas):
			valoresX=[]
			for j in range(0,self.filas):
				valor=tinas.aleatorio(self)
				if valor <= 0.5:
					x=self.valor_a + sqrt(self.k1 * valor)
				else:
					x=self.valor_b-sqrt(self.k3*(1-valor))
				valoresX.append(x)
			contador+=1 if (sum(valoresX)<=1000) else 0
		self.probabilidad=(contador/self.columnas)*100

x=tinas(sys.argv[1:])

print("Probabilidad: {0:.4f}".format(x.probabilidad)+"%")




