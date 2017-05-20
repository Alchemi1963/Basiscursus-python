#Wat zijn de getallen?
getal1 = 50
getal2 = 20
getal3 = 25
getal4 = 5
getal5 = 100
getal6 = 2

#Sla de sommen als variabele op
som1 = 'Wat is ' + str(getal1) + ' + ' + str(getal2) + '?:		'
som2 = 'Wat is ' + str(getal3) + ' / ' + str(getal4) + '?:		'
som3 = 'Wat is ' + str(getal5) + ' ^ ' + str(getal6) + '?:		'

#Bereken de antwoorden
ant1 = getal1 + getal2
ant2 = getal3 / getal4
ant3 = getal5 ** getal6

#Vraag de antwoorden
usr1 = int(input(som1))
usr2 = int(input(som2))
usr3 = int(input(som3))
if usr1 == ant1 and usr2 == ant2 and usr3 == ant3: #Kijk of alles goed is
	print('Gefeliciteerd!')

else:
	if usr1 != ant1: #Is vraag 1 fout?
		print('Je had de eerste som fout...')

	if usr2 != ant2: #Is vraag 2 fout?
		print('Je had de tweede som fout...')

	if usr3 != ant3: #Is vraag 3 fout?
		print('Je had de derde som fout...')
