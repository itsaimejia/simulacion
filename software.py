#! /usr/bin/python
#-*- coding:utf-8 -*-
#
#Validacion de software empleando numeros pseudoaleatorios
#el usuario debe ingresar la cadena a validad mediante el 
#parametro -l o -licencia
#Se emplea el metodo congruencial multiplicativo
#
#Itsai Mejia
#Sep 10, 2019
#al16760300.AT.ite.DOT.edu.DOT.mx
#

#llamado a liberias
import sys, getopt, argparse
###

#Se crea la clase a ser ejecutada
class software: 
	def __init__(self, datos):
		self.datos=datos
		try:
			opts,args=getopt.getopt(self.datos,"hL:",["help","licencia="])
		except getopt.error:
			print ('Modo de ejecutar el codigo:')
			print ('software.py -L <licencia> ')
			print ('   ')
			print ('Escriba solamente software.py -h para mayor informacion ')
			sys.exit(2)
		for opt,arg in opts:
			if opt in ("-h","--help"):
				parser=argparse.ArgumentParser(description='''
					El programa permite determinar si la cadena ingresada pertenece 
					a un software legal, empleando el metodo de generador de 
					numero pseudoaleatorio.
					El metodo requiere el ingreso de una cadena en el formato
					M-A-B-C-N-E
					Donde:
					M es el modulo
					A y B son los terminos para la formula (AXn+B) mod M
					C representa la semilla (valor inicial),
					N secuencia a generarse y por ultimo
					E es el pseudo aleatorio obtenido empleando esta tecnica.
					Cada valor es una cadena en forma hexadecimal.
					''', epilog='''
					Al generar el N-esimo termino de la sucesion, co concuerda 
					con el valor E, quiere decir que la cadena es valida y por lo
					tanto es un software legal. 
					''')
				parser.add_argument('-L','--licencia', help='Cadena de la licencia de software', required=True)
				args=parser.parse_args()
			elif opt in ("-L","--licencia"):
				self.licencia=arg
		software.valida(self)

	def valida(self):
		cadena_ingresada=self.licencia.split('-') #separar en cada dato ingresado
		valores_decimales=list(map(lambda x: int(x,16),cadena_ingresada)) #convertir de hexadecimal a decimal
		semilla=valores_decimales[3]
		for i in range(1, valores_decimales[4]+1):
			x=(valores_decimales[1]*semilla+valores_decimales[2])%valores_decimales[0]
			semilla=x
			
		if x==valores_decimales[5]:
			self.legal=1
		else:
			self.legal=0

x=software(sys.argv[1:])

if x.legal==1:
	print ('Su software ha sido validado')
else:
	print ('Tenemos un problema con su licencia; por el momento, no fue validado')