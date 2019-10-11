#!/usr/bin/python
#
# Generador de licencias en hexadecimal
#
import sys, getopt, argparse

def licencia(datos):
	valores=datos.split('-')
	m=int(valores[0]) #modulo
	a=int(valores[1]) #termino a
	b=int(valores[2]) #termino b
	c=int(valores[3]) #semilla
	n=int(valores[4]) #secuena a generarse
	semilla=c
	for i in range(0,n):
		e=((a*semilla)+b)%m
		semilla=e
	print("PARAMETROS: ")
	print("M: {}\nA: {}\nB: {}\nC: {}\nN: {}\nE: {}".format(m,a,b,c,n,e))
	licencia=str("{0:x}-{1:x}-{2:x}-{3:x}-{4:x}-{5:x}".format(m,a,b,c,n,e)).upper()
	print("Licencia: {}".format(licencia))


cadena=sys.argv[1:]
datos=""


opts,args=getopt.getopt(cadena,"hC:",["help","cadena="])
for opt,arg in opts:
	if opt in ("-h","--help"):
		parser=argparse.ArgumentParser(description='''
			El programa genera una licencia en base a datos ingresados
			por el usuario, estos datos requieren un formato de la forma:
			M-A-B-C-N
			M es el modulo
			A y B son los terminos para la formula (AXn+B) mod M
			C representa la semilla (valor inicial),
			N secuencia a generarse 
			Nota: todo son valores numericos
			''', epilog='''
			El programa devuelve una cadena con el formato
			M-A-B-C-N-E todo esto con valores hexadecimales
			donde hasta -N son los mismos datos explicados
			con la variación de E que es el pseudo aleatorio obtenido empleando 
			la tecnica. 
			''')
		parser.add_argument('-C','--cadena',help='Cadena de los datos a evaluar', required=True)
		args=parser.parse_args()
	elif opt in ("-C","--cadena"):
		datos+=arg

licencia(datos)

