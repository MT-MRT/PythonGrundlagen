#In der letzen Aufgabe haben wie allgemeinn gelernt wie man eine Variable nutzt und die string Variable eingeführt, nun beschäftigen wir uns mit allen anderen möglichen Variablentypen

"""
Python macht dem Nutzer die Nutzung von Variablen sehr leicht. So muss man beim Deklarieren der Variablen in Java erst den Datentyp der Variable definiern z.b "int zahl = 3;" , eine Typdeklaration wie diese ist in Python nicht nötig. 
In Python werden Varaiablen in eine von drei Kategorien einsortiert:
1. string 
  (z.b variablennamen1 = "Inhalt")
2. Zahl 
  (z.b variablennamen2 = 10 oder variablennamen2 = 8.54)
3. Boolean - wahr/falsch 
  (z.b ist_wahr = True oder ist_falsch = False)

Aufgabe: Deklariere die Variable die im Text genannt werden für Namen, Bauteilanzahl und Höchstgeschwindigkeit an.
"""

print(roboter_name)
print(anzahl_bauteile)
print(geschwindigkeit_hoechst)

print("Der Name des Roboters ist " + roboter_name + ".")
print(roboter_name + " wurde aus " + str(anzahl_bauteile) + " Bauteilen gebaut.")
print("Der Roboter besteht zwar nur aus " + str(anzahl_bauteile) + " besteht ist die Höchstgeschwindigkeit von " + roboter_name + " " + str(geschwindigkeit_hoechst) + "km/h.")

#Notiz: Du fragt dich warum in dem Text vor dem Abrufen einiger Variablen ein str() steht? Das liegt daran, dass es sonst Probleme gibt, da wir hier mit string und einer Zahl gleichzeitig arbeiten. Daher muss man explizit sagen, dass man hier eine Zahl hat, welche als Text ausgedruckt werden soll. 
#Mach das str() doch mal weg und schau dir die Fehlermeldung an und behalte dir, dass du immer wenn du mit sting und einer Zahl gleichzeitig arbeitest immer explizit sagen muss das die Zahl als Text ausgedruckt werden soll werden soll.
