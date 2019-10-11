#!/usr/bin/python
#
# Generador de contrasena segura
#
from aleatorio import genera 
from datetime import datetime
import math

def hacer(cuantos):
	may=["B","D","E","G","H","L","N","P","R","V"]
	minu=["a","c","d","e","f","i","l","m","o","r","s","u","z"]
	contra=[]
	for x in range(1,cuantos+1):
		ahora=datetime.now()
		valor=genera(ahora.microsecond)
		if valor <= 0.5:
			#May
			ahora2=datetime.now()
			valor2=genera(ahora2.microsecond)
			y=int(len(may)-1*valor2)
			contra.append(may[y])
		else:
			#Min
			ahora3=datetime.now()
			valor3=genera(ahora3.microsecond)
			y=int(len(minu)-1*valor3)
			contra.append(minu[y])
	return(contra)

def realizar(longitud):
	if longitud <= 0:
		print("Intenta con otro valor")
	else:
		passa=hacer(longitud)
		print(passa)


def main():
	while True:
		try:
			n=int(input("Numero de caracteres para la contrasena: "))
			break
		except:
			print("Debe seleccionar otro valor")
	realizar(n)

if __name__=="__main__":main()