#!/usr/bin/python
#
# Generador dos de pseudoaleatorio
#
from decimal import *

a=895
b=542
c=1101

def genera(semilla):
	m=(a*semilla+b)%c
	aleatorio=Decimal(m)/c
	return(aleatorio)