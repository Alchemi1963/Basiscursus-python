import os

#Negeer dit; deze is nodig om hem te laten werken op Windows
import sys
def clear():
	if 'win' in sys.platform:
		os.system('cls')
	else:
		os.system('clear')

#Nu niet meer negeren
cijferlijst = [] #Maak de lijst

while True: #Zorg dat dit blijft draaien
	clear() #leeg het scherm
	start = input('Wat wil je doen?\n\
	\t1) Een cijfer toevoegen\n\
	\t2) Een cijfer verwijderen\n\
	\t3) Je cijferlijst zien\n\
	\t4) Je gemiddelde cijfer zien\n\
	\t5) Je hoogste en laatste cijfer zien\n\
	\t6) De lijst leeg maken\n') #Laat de gebruiker een keuze maken
	clear() #Leeg het scherm

	#De opties
	if start == '1':
		cijfer = input('Wat is het cijfer?\n') #Vraag naar het nieuwe cijfer
		cijferlijst.append(cijfer) #Voeg dat toe aan de lijst
		continue #Terug naar het begin

	elif start == '2':
		print('\n'.join(cijferlijst)) #Print de lijst mooi (zie de tip)
		cijferx = input('Welk cijfer wil je verwijderen?\n') #Vraag welk cijfer de gebruiker wil verwijderen
		if cijferx in cijferlijst: #Check of dat cijfer wel in de lijst zit
			cijferlijst.remove(cijferx) #Haal dat cijfer weg
		continue #Terug naar het begin

	elif start == '3':
		print('\n'.join(cijferlijst)) #Print de lijst mooi (zie de tip)
		input('Druk op ENTER om door te gaan...') #Zorg ervoor dat de code niet meteen doorgaat
		continue #Terug naar het begin

	elif start == '4':
		i = 0
		gemiddelde = 0

		while i != len(cijferlijst): #Tel alle cijfers uit de lijst op in een variabele
			gemiddelde += int(cijferlijst[i])
			i += 1

		gemiddelde /= len(cijferlijst) #Deel die variabele door het aantal cijfers in de lijst en sla dat op
		print(gemiddelde) #Print die variabele
		input('Druk op ENTER om door te gaan...')
		continue #Terug naar het begin

	elif start == '5':
		hoog = cijferlijst[0] #Hoogste cijfer is eerste cijfer
		laag = cijferlijst[0] #Laagstse cijfer is eerste cijfer
		i = 0

		while i != len(cijferlijst) and len(cijferlijst) > 1: #Ga door totdat je alle cijfers in de lijst heb gehad
			if int(cijferlijst[i]) > int(hoog): #Bekijk of het huidige cijfer groter is dan je huidige hoogste cijfer
				hoog = cijferlijst[i] #Als dat zo is, maak het huidige cijfer het huidige hoogste cijfer

			elif int(cijferlijst[i]) < int(laag): #Bekijk of het huidige cijfer kleiner is dan je huidige laagste cijfer
				laag = cijferlijst[i] #Als dat zo is, maak het huidige cijfer het huidige laagste cijfer
			i += 1

		print('Je hoogste cijfer is een', hoog)
		print('En je laagste cijfer is een ', laag)
		input('Druk op ENTER om door te gaan...')
		continue #Terug naar het begin

	elif start == '6':
		cijferlijst = [] #Sla de cijerlijst opnieuw op als een lege lijst
		continue #Terug naar het begin
	
	else:
		print('Dit is geen optie...')
		input('Druk op ENTER om verder te gaan...')
		continue #Terug naar het begin
