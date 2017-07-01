#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 2016-06-30 

# Author: RootWeiller

'''Escribir una función que tome un carácter 
y devuelva True si es una vocal, de lo contrario devuelve False.'''


def Letters():

	x = input("Ingrese la letra: ")

	if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":

		print ("Si, es una vocal", x)

	elif x=="A" or x=="E" or x=="I" or x=="O" or x=="U":

		print ("Si, es una vocal", x)

	else:

		print ("Esto no es una vocal", x)


Letters()