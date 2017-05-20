##Opdracht:
##Maak een programma dat een willekeurig vermenigvuldigings-som maakt, dus elk_getal * elk_ander_getal en dat vijf keer doet en de som + het antwoord print.
##Maar na elke print moet hij het scherm legen, na 2 seconden.
import os, random, time

i = 0
while i < 5:
	getal1 = random.randrange(-10,11)
	getal2 = random.randrange(-10,11)
	antwoord = getal1 * getal2
	print(getal1,'*',getal2,'=',antwoord)
	i += 1
	time.sleep(2)
	os.system('cls')
