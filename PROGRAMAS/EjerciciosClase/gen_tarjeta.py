#!/usr/bin/python
#
# Generador de tarjetas
#
def primerosCuatro(numero):
	while(numero>9999):
		numero=numero/10
	return int(numero)

def numero(semilla, limite, a, c):
	xn=semilla
	for x in range(0,limite):
		xi=(a*xn)%c
		xn=xi
	return primerosCuatro(xn)

def generadorTarjeta(semilla, t, d,bandera):
	tarjeta=[semilla]
	#valores definidos
	a=8*t+3 if (bandera==1) else 8*t-3 
	c=2**d

	#iteraciones
	n1=semilla/1000
	aux=semilla%1000
	n2=aux/100
	aux=aux%100
	n3=aux%10

	#lista de numeros
	tarjeta.append(numero(semilla,int(n1),a,c))
	tarjeta.append(numero(semilla,int(n2),a,c))
	tarjeta.append(numero(semilla,int(n3),a,c))

	return tarjeta

def main():
	semilla= int(input("Ingresa la semilla: "))
	t=int(input("Valor de t: "))
	d=int(input("Valor de d: "))
	bandera=int(input("Ingresa la bandera (1/0):(+/-): "))


	print("Tu tarjeta es: %s"%generadorTarjeta(semilla,t,d,bandera))
	
if __name__=="__main__":main()
