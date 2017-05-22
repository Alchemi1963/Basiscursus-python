##Opdracht:
##Maak de opdracht van H7 opnieuw, maar dit keer met functies.
##En zorg er ook voor dat je kan stoppen, meerdere cijfers in een keer kan doen (toevoegen en verwijderen).

import os

#Negeer
import sys
def clear():
	if 'win' in sys.platform:
		os.system('cls')
	else:
		os.system('clear')
#Ga weer verder

def nieuwCijfer(cijferlijst):
	cijferlijst.append(int(input('Voeg een cijfer toe:\n')))
	while True:
		cijfer2 = input('Voeg nog een cijfer toe, druk anders op ENTER:\n')
		if cijfer2 != '':
			cijferlijst.append(int(cijfer2))
		else:
			break
	
	return cijferlijst

def printCijfers(cijferlijst):
	for cijfer in cijferlijst:
		print(cijfer)
	
def xCijfer(cijferlijst):
	print('Welk cijfer wil je verwijderen?')
	printCijfers(cijferlijst)
	cijfer = int(input())
	
	if cijfer in cijferlijst:
		print('Je',cijfer,'is verwijderd')
		cijferlijst.remove(int(cijfer))
		ENTER()
	else:
		print('Er zit geen',cijfer,'in je cijferlijst')
		ENTER()
	
	return cijferlijst


def gemCijfer(cijferlijst):
	gemiddeld = 0
	for cijfer in cijferlijst:
		gemiddeld += cijfer
	gemiddeld /= len(cijferlijst)
	return gemiddeld

def hoogLaagCijfer(cijferlijst):
	hoog = cijferlijst[0]
	laag = cijferlijst[0]
	for cijfer in cijferlijst:
		if cijfer > hoog:
			hoog = cijfer
		elif cijfer < laag:
			laag = cijfer
	return hoog, laag

def leegLijst():
	cijferlijst = []
	return cijferlijst

functies = [[nieuwCijfer, 'Voeg cijfers toe'], [xCijfer, 'Verwijder cijfers'], [printCijfers, 'Bekijk je cijfers'], [gemCijfer, 'Bekijk je gemiddelde'], [hoogLaagCijfer, 'Bekijk je hoogste en je laagste cijfer'], [leegLijst, 'Leeg je cijferlijst'], ['break', 'Stop het programma']]

def ENTER():
	input('Druk op ENTER om verder te gaan...')

def start():
	cijfers = []
	while True:
		clear()
		print('Wat wil je doen?')
		for functie in functies:
			print(functies.index(functie) ,functie[1])
		actie = input()
		
		functies[int(actie)][0](cijfers)
		
		clear()

start()
