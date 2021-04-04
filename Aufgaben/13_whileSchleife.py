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
Schreibe ein Programm, welches vier gerade Zahlen von Nutzer annimmt und diese dann in einer Liste schreibt, welche am Ende ausgegeben wird. Dabei soll wenn eine ungerade Zahl angegeben ausgegeben werde, das die eingegebene Zahl keine gerade Zahl ist und die Zahl soll somit erst in die Liste eingetragen werde wenn sie gerade ist. 
Tipp: Dafür brauchst du eine while-Schleife die bis vier geht und darin eine if-Abfrage.
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############

