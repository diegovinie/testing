#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from time import sleep
import sys
from terreno import genTerr, genMap, printMap

''' Pequeño programa de simulación del vuelo de un avión. 
Se define la:
	clase Nave:
		atributos: 
			nombre
			posición
			altura
			combustible
			motor
		metodos:
			Despegar
			Aterrizar
			Ascender
			Descender
			Potencia
			Ver
			Status

	Función Avanzar: la cual mueve la nave horizontalmente e indica si choca con el terreno.

	La función Controles: donde están los controles de navegación.

	El terreno se genera con las funciones de terreno.py

@author: Diego Viniegra


'''
#--------FUNCION AVANZAR------------

def Avanzar(nave):
	'''Avanza y relaciona la nave con el terreno'''
	nave.pos += 1
	if nave.h <= terreno[nave.pos]:
		print '\nChoque!\n'
		Ma = genMap(terreno)
		Ma[nave.h][nave.pos] = '*'
		printMap(Ma,terreno)
		raw_input('Pulse ENTER tecla para salir')
		sys.exit(0)
	else: pass


#----------AVION------------------

class Nave(object):
	def __init__(self, nombre, fuel, pos=0):
		self.nombre = nombre
		self.fuel = fuel
		self.h = 0
		self.pos = pos
		print 'Nombre: ', self.nombre
		print 'Posición: ', self.pos, 'm'		
		print 'Altura: ', self.h, 'm'
					
	def Despegar(self):
		if self.h == 0:
			print "Despegando\n"
			self.h = 1
			self.pos += 1
			self.motor = 100
			self.fuel -= 0.05*self.motor
		else:
			print 'ya en el aire'

	def Aterrizar(self):
		if self.h == 1:
			print 'Aterrizando\n'
			self.h = 0
			self.pos += 1
			self.fuel -= 0.05*self.motor
		elif self.h == 0:
			print 'ya en tierra'
		elif self.h > 1:
			print 'muy alto'
	def Ascender(self):
		if self.h == 5:
			print '\ntecho de servicio\n'		
		else:
			self.h += 1
			print 'Ascendiendo\nAltura: ', self.h, '\n'
		self.fuel -= 0.05*self.motor
		Avanzar(self)


	def Descender(self):
		self.h -= 1
		self.fuel -= 0.05*self.motor
		Avanzar(self)
		print 'Descendiendo\nAltura: %d\n' % self.h

	def Status(self):
		print 'Status:\nAltura: %d\nPosición: %d\nCombustible: %d\n' % (self.h, self.pos, self.fuel)

	def Potencia(self,motor):
		self.motor = motor
		self.fuel -= 0.05*self.motor
		Avanzar(self)
		print 'Motor a', self.motor, '%'

	def Ver(self):
		'''Devuelve el terreno en las 4 casillas siguientes siempre que no se solape la vista'''

		Ma = genMap(terreno)
		Ma[self.h][self.pos] = '>'
		printMap(Ma,terreno)


# ---------CONTROLES------------

def Controles(nave):
	ti = 0
	while True:
		if	nave.h == 0:
			print "\nControles:"
			print "v: Ver Firmamento\ns: Ver Status\nt: Despegar\n\nq: Para salir\n"
			x = raw_input('Seleccione su acción: ')
			print '\n'
		
			if x == 'v':	
				nave.Ver()
		
			elif x == 's':
				nave.Status()
		
			elif x == 't':
				nave.Despegar()
			elif x == 'q':
				print 'Hasta nunca'				
				sys.exit(0)	
			else:
				continue

		elif nave.h > 0:
			print "Controles:"
			print "v: Ver Firmamento\ns: Ver Status\nl: Aterrizar\na: Ascender\nd: Descender\np: Potencia\n\nq: Para salir\n"

			x = raw_input('Seleccione su acción: ')
			print '\n'
		
			if x == 'v':	
				nave.Ver()
		
			elif x == 's':
				nave.Status()
	
			elif x == 'l':	
				nave.Aterrizar()
	
			elif x == 'p':
				mot = input('Seleccione potencia: ')		
				nave.Potencia(mot)
	
			elif x == 'a':
				nave.Ascender()
	
			elif x == 'd':
				nave.Descender()

			elif x == 'q':
				print 'Hasta nunca'				
				sys.exit(0)	

			else:
				continue
		else: pass

#-----OPENING---------
print '\n\n\n\nWelcome to the new: \n\nFLIGHT SIMULATOR: TRAFFICANT EDITION\nver: 0.1\n\nWrited by Diego Viniegra while on holydays\n\n'
print '________________________________________'

	
#------AREA DE PRUEBAS------------


name = raw_input('Seleccione su avión: ')
fuel = input('Seleccione su combustible: ')	
# terreno = funTerr()
terreno = genTerr()
avion1 =Nave(name, fuel)
Controles(avion1)

