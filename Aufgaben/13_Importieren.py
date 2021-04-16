print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#hier wird der Import von externen Paketen erklärt

'''
Es gibt die Möglichkeit externe Module in das eigene Programm einzubinden. Dafür muss man die Module mit dem Keyword "import" importieren, dieses wird immer als oberster Befehl in ein Programm geschrieben. Hat man ein Modul importiert, so kann man die darin vorhandenen Funktionen nutzen. Da die Funktion aus dem importierten  Modul kommt, kann man die Funktion nicht einfach nur mit dem Funktionsnamen aufrufen, sondern muss noch den Modulnamen davorschreiben.
Hier ein Beispiel:
''' 
import math
print("PI ist: " + str(math.pi))
'''
Wie die Funktionen in den importierten Modulen heißen und was diese an Parametern brauchen, findet man am einfachsten durch eine kurze Google-Suche heraus.

Aufgabe:
Importiere die Module "time" und "random".
In "time" gibt es die Funktion ".sleep()" mit der man das Fortlaufen des Programms verzögert. Als Parameter wird hier eine Zeit in Sekunden angegeben.
Mit "random" kann man Zufallszahlen erstellen. Wir nutzen hier die Funktion ".randint()". In den Klammern von randint werden zuerst der Anfangswert und dann der Endwert der Menge, aus der die Zufallszahl generiet werden soll, übergeben (Beispiel das Erstellen eines zufälligen Würfels: würfel = random.randint(1,6)).
Nutze nun die ".randint()" Funktion und erstelle eine Zufallszahl zwischen zwei und sieben, gebe diese im Anschluss aus.
Schreibe dann eine for-Schleife, die sooft wie die Zufallszahl hoch ist durchläuft. In der Schleife befinden sich zwei Ausgaben, die erste gibt den Durchlauf der Schleife an (also die Höhe der Zählvariablen). Die zweite Ausgabe soll mit ".sleep()" um 3 Sekunden verzögert kommen und "Diese Ausgabe ist verzögert" ausgeben.
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############
