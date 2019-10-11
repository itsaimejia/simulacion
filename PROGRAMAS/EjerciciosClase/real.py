#!/usr/bin/python
#
# Generador dos de pseudoaleatorio
#
from aleatorio import genera
from datetime import datetime

ahora=datetime.now()
aux=genera(ahora.microsecond)
print("{:0.4f}".format(aux))