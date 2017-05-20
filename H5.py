##Opdracht:
##Maak een programma dat de tafel van elk getal dat de gebruiker geeft kan berekenen.
##Gebruik hiervoor een while loop.
##Extra: pas het zo aan dat de tafel doorgaat tot 120


cijfer = int(input('Van welk getal wil je de tafel weten?')) #Vraag getal waarvoor je de tafel maakt

vermenigvuldiger = 1 #Maak een variabele "vermenigvuldiger" aan met waarde 1

while vermenigvuldiger < 13: #Zolang vermenigvuldiger onder de 13 zit, voer dit hieronder uit
	getal = cijfer*vermenigvuldiger #Bereken getal met het cijfer * de vermenigvuldiger
	print(str(vermenigvuldiger),'*', str(cijfer),'=',getal) #print "vermenigvuldiger * cijfer = getal"
	vermenigvuldiger += 1 #Tel 1 op bij vermenigvuldiger
