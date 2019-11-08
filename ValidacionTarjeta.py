#! /usr/bin/python
#-*- coding:utf-8 -*-
#
#Validacion de tarjeta que el cliente
#infiere fue duplicada, en caso que la tarjeta fue
#duplicada, en caso que fue duplicada la aseguradora pagara
#el indicente, en caso que no la aseguradora no hara nada
#
#
#Itsai Mejia
#Nov 07, 2019
#al16760300.AT.ite.DOT.edu.DOT.mx
#

#llamado a liberias
import sys, getopt, argparse
###

#Se crea la clase a ser ejecutada
class validador: 
	def __init__(self, datos):
		self.datos=datos
		self.semilla=5883
		self.a=329
		self.m=262144
		try:
			opts,args=getopt.getopt(self.datos,"hT:",["help","tarjeta="])
		except getopt.error:
			print ('Modo de ejecutar el codigo:')
			print ('ValidacionTarjeta.py -T <numero_tarjeta> ')
			print ('   ')
			print ('Escriba solamente ValidacionTarjeta.py -h para mayor informacion ')
			sys.exit(2)
		for opt,arg in opts:
			if opt in ("-h","--help"):
				parser=argparse.ArgumentParser(description='''
					El programa permite determinar si la tarjeta otorgada por el cliente
					es valida comparandola con la tarjeta generada internamente. 
					Esta tarjeta es generada usando el metodo de numeros pseudoaleatorios
					''', epilog='''
					Al hacer la validacion de la tarjeta y esta es correcta el
					programa le muestra al usuario el resultado de su validez
					y genera una nueva tarjeta para el cliente independiente si es valida o no
					''')
				parser.add_argument('-T','--tarjea', help='Numero de tarjeta a validar', required=True)
				args=parser.parse_args()
			elif opt in ("-T","--tarjeta"):
				self.tarjetaIngresada=arg

		validador.valida(self)

	def primerosCuatro(numero):
		while(numero>9999):
			numero=numero/10
		return int(numero)

	def aleatorio(self,semilla,limite):
		xn=semilla
		for x in range(0,limite):
			xi=(self.a*xn)%self.m
			xn=xi
		return validador.primerosCuatro(xn)

	def generadorTarjeta(self):

		#iteraciones
		n1=self.semilla//1000
		aux=self.semilla%1000
		n2=aux//100
		aux=aux%100
		n3=aux%10

		#lista de numeros
		#numero 1
		digito2=validador.aleatorio(self,self.semilla,n1)
		#numero 2
		digito3=validador.aleatorio(self,digito2,n2)
		#numero 3
		digito4=validador.aleatorio(self,digito3,n3)

		return str("{0}-{1}-{2}-{3}".format(self.semilla,digito2,digito3,digito4))

	def valida(self):
		self.tarjetaGenerada=validador.generadorTarjeta(self)
		self.esValida = 1 if(self.tarjetaGenerada==self.tarjetaIngresada) else 0
		self.semilla=5517
		self.nuevaTarjeta=validador.generadorTarjeta(self)

		

x=validador(sys.argv[1:])

if x.esValida==1:
	print("La tarjeta es valida")
	print("Por seguridad, su nuevo numero de tarjeta: %s"%x.nuevaTarjeta)
else:
	print("La tarjeta ha sido clonada")
	print("La tarjeta real es: %s"%x.tarjetaGenerada)
	print("La que se ingreso es: %s"%x.tarjetaIngresada)
	print("Los numeros presentan incongruencias")
	print("Su nuevo numero de tarjeta es: %s"%x.nuevaTarjeta)