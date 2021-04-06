print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#Dies ist die Fortsetzung von dem Abschnitt über Funktionen. Hier lernen wir wie man Parameter in eine Funktion einbindet

'''
Bisher haben wir Funktionen nur dazu eingesetzt, dass sie die Nutzung von redundante Ausgabebefehle erleichtern. Nun lernen wir, wie man Parameter in eine Funktion einbindet. 
Ein Parameter ist eine Variable, welche die Eingabe aus dem Funktionsaufruf in den Programmcode im Funktionskörper überträgt. 
Hier ein Beispiel:
'''

def halloName(name):
  print("Hallo " + name + ". Willkommen!")

halloName("Sam")
halloName("Sabrina")

'''
Wichtig ist, dass sobald man ein Parameter in eine Funktion einbringt, dieser Wert auch beim Funktionsaufruf übergeben werden muss. Probier es mal aus und lösche "Sabrina", nun wird beim Ausführen eine Fehlermeldung kommen.
Wenn man mehr als ein Parameter in eine Funktion einbringen möchte, so werden diese durch Kommata getrennt hintereinander in die jeweilige Klammer geschrieben. Zum Beispiel: def hello(name, alter) und passend dazu beim Funktionsaufruf hallo("Sina", 23).

Aufgabe: Schreibe eine Funktion die den Namen, den Studiengang und das Semester von einem Studenten annimmt und diese in einem sinvollen Satz ausgibt. Rufe diese Funktion dann mit drei verschiedenen Studenten auf. 
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############

