print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#jetzt lernen wir noch die while Schleife kennen

'''
Eine while-Schleife wird so lange durchlaufen bis das Abbruchkriterium erreicht ist. Das Abbruchkriterium ist meist eine bestimme Anzahl an Schleifendurchläufen welche über eine Zählvariable, wie zuvor in der for-Schleife, gezählt werden.
Wichtig ist in der while-Schleife muss die Zählvariable im Schleifenkörper um eins hochgestuft werden, denn sonst wird der Abbruchwert nie erreicht und man kreiert eine Endlosschleife. 
Hier ein Beispiel:
'''
durchgang = 1
while durchgang < 11:
    print(durchgang)
    durchgang+=1
print("Die Schleife ist beendet.")

'''
Aufgabe:
Schreibe ein Programm, welches vier gerade Zahlen vom Nutzer annimmt und diese dann in einer Liste schreibt, welche am Ende ausgegeben wird. Dabei soll, wenn eine ungerade Zahl angegeben wird, ausgegeben werden, dass die eingegebene Zahl keine gerade Zahl ist und die Zahl soll nicht in die Liste eingetragen werden. Dies ist also so oft zu wiederholen, bis 4 gerade Zahlen vorhanden sind.
Tipp: Dafür brauchst du eine while-Schleife und darin eine if-Abfrage. Denk dran, dass in der if-Abfrage der Befehl dann nochmal weiter eingerückt werden muss.
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############

