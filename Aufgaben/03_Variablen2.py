print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#In der letzten Aufgaben haben wir allgemein gelernt, wie man eine Variable nutzt und die String Variable eingeführt, nun beschäftigen wir uns mit allen anderen möglichen Variablentypen

"""
Python macht dem Nutzer die Nutzung von Variablen sehr leicht. So muss man beim Deklarieren der Variablen in Java erst den Datentyp der Variablen definiern z.b "int zahl = 3;" , eine Typdeklaration wie diese ist in Python nicht nötig. 
In Python werden Varaiablen in eine von drei Kategorien einsortiert:
1. String 
  z.B variablennamen1 = "Inhalt"
2. Zahl 
  z.B variablennamen2 = 10 oder variablennamen2 = 8.54
3. Boolean - wahr/falsch 
  z.B ist_wahr = True oder ist_falsch = False

Aufgabe: Deklariere die Variablen die im Text genannt werden für Namen, Bauteilanzahl und Höchstgeschwindigkeit, sodass die Ausgabe funktioniert.
"""
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############

print(roboter_name)
print(anzahl_bauteile)
print(geschwindigkeit_hoechst)

print("Der Name des Roboters ist " + roboter_name + ".")
print(roboter_name + " wurde aus " + str(anzahl_bauteile) + " Bauteilen gebaut.")
print("Der Roboter besteht zwar nur aus " + str(anzahl_bauteile) + " besteht ist die Höchstgeschwindigkeit von " + roboter_name + " " + str(geschwindigkeit_hoechst) + "km/h.")

# Notiz: Du fragt dich warum in dem Text vor dem Abrufen einiger Variablen ein str() steht? Das liegt daran, dass es sonst Probleme gibt, da wir hier mit einem String und einer Zahl gleichzeitig arbeiten. Daher muss man explizit sagen, dass man hier eine Zahl hat, welche als Text ausgegeben werden soll. 
# Lösche das "str()" einmal und schaue die Fehlermeldung an. Man muss immer daran denken, wenn man mit einer Zahl und einem String gleichzeitg arbeitet, die Zahl muss für die Ausgabe in einem String umgewandelt werden.
