print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#In dieser Aufgabe geht es um das if Statement

'''
Nun kommen wir zu Fallunterscheidungen. Mit einen if Statement können wir unter einer Bedingung Aktionen einleiten. Ist die Bedingung nicht wahr, so wird die Aktion darunter einfach übersprungen. 
Ein if Statement wird mit dem Kennwort "if" eingeleitet, danach folgt die Bedingung und am Ende der Bedingung ein Doppelpunkt. Wie bei den Funktionen ist die Anweisung darunter eingerückt. 

Hier wird überprüft, ob die Zahl aus der Eingabe größer 10 ist. Ist Zahl nicht größer als 10 so passiert nichts, ist sie größer so wird sie mit einem kleinen Text zusammen nochmals ausgegeben.
'''

print("Gib hier eine beliebige Zahl ein:")
zahl = int(input())

if zahl > 10:
  print("Die eingegebene Zahl " + str(zahl) + " ist größer als 10.")

'''
Für den Vergleich werden die sogenannten Vergleichsoperatoren genutzt:
< kleiner als
> größer als
== gleich
<= kleiner gleich 
>= größer gleich 
!= nicht gleich

Aufgabe: Schreibe ein if Statment, welches prüft ob eine Zahl durch zwei ohne Rest teilbar ist. Ist die Zahl ohne Rest teilbar, so soll sie wieder eingebunden in einen kurzen Satz ausgegeben werden. (Tipp: Nutze den Modulo Operator %, z.B.: 10 % 3 = 1)
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############
