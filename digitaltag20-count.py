#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

print("Digitaltag20-count: Wie viele Stunden Programm hatte der Digitaltag 2020?\n")

print("Lese die Website ein.")
# Die Website https://www.digitaltag.eu wurde im Browser geöffnet und das Aktionsprogramm angezeigt.
# Es wurden "Alle Veranstaltungen" gefiltert und die Website mit "Speichern" als HTML-Quelltext als website.html gesichert.
with open("website.html") as f:
	data=f.read()

dauer=[] # enthält die Dauer jeder einzelnen Veranstaltungen als String, so wie er auf der Website angezeigt wird
while data.find('<span class="zeit">')>-1: # die Dauer befindet sich in diesem HTML-Tag in der Form "ganztägig" oder z.B. "14:00 - 15:00 Uhr"
	data=data.split('<span class="zeit">',1)[1]
	zeit=data.split('</span>',1)[0]
	dauer.append(zeit.strip())
	data=data.split('</span>',1)[1]

print("Es wurden",len(dauer),"Veranstaltungen gefunden.")

minuten=0 # enthält die Dauer aller Veranstaltungen in Minuten
anz_ganztaegig=0 # enthält die Anzahl der ganztägigen Veranstaltungen
for termin in dauer:
	if termin=="ganztägig": # es gibt ganztägige Termine 
		minuten=minuten+300 # ganztägige Termine werden mit einer durchschnittlichen Dauer von 5h angenommen
		anz_ganztaegig=anz_ganztaegig+1
	else: # ... alle anderen haben eine Dauer in der Form von z.B. "15:00 - 16:30 Uhr"
		anfang=termin.split(" ",1)[0] # das könnte man mit einem regulären Ausdruck sehr viel schöner machen als den String stumpf zu zerlegen. Aber es erfüllt seinen Zweck.
		ende=termin.split("- ",1)[1]
		ende=ende.split(" ",1)[0]
		FMT="%H:%M"
		tdelta=datetime.strptime(ende,FMT)-datetime.strptime(anfang,FMT)
		minuten=minuten+int(tdelta.seconds/60)

print("Davon waren",anz_ganztaegig,"ganztägig.\n")

# Finales Ergebnis ausgeben
print("Insgesamt hat das Programm des Digitaltages 2020 damit",round(minuten/60),"Stunden gedauert.")
