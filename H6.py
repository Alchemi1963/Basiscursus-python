##Opdracht:
##Schrijf een programma dat met 2 willekeurige getallen een vermenigvuldiging maakt en de som + het antwoord print, dit moet hij 5 keer uitvoeren.
##Zorg er ook voor dat hij na elke print, 2 seconden wacht en dan het scherm leegt.
##Extra: pas het programma zo aan dat hij dit een willekeurig aantal keer doet.

import os, random, time #Importeer de os, de random en de time module

i = 0 #Zet de teller op 0
while i < 5: #Ga door totdat de teller op vijf staat
	getal1 = random.randrange(-10,11) #Genereer getal 1 met een range van -10 t/m 10
	getal2 = random.randrange(-10,11) #Genereer getal 2 met een range van -10 t/m 10
	
	antwoord = getal1 * getal2 #Bepaal de uitkomst
	print(getal1,'*',getal2,'=',antwoord) #Print de som met de uitkomst
	i += 1 #Update de teller
	
	time.sleep(2) #Pauzeer voor 2 seconden
	os.system('cls') #Leeg het scherm
	continue #Terug naar het begin
