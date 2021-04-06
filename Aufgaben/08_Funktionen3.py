print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#Dies ist die Fortsetzung von dem Abschnitt über Funktionen. Hier lernen wir wie man eine Rückgabe von Funktionen erhält. 

'''
In den letzten Aufgaben haben wir immer eine direkte Ausgabe in der Funktion gehabt. Damit wir aber auch mit den Werten, die von der Funtkion erzeugt werden, weiterarbeiten können brauchen wir das return Statement.
Das return Statement steht am Ende der Funktion. Nach dem return Statement steht die Variable, welche wir zurückgeben wollen. Alles was in der nächsten Zeile nach einem return Statement geschrieben wird, wird nicht mehr vom Interpreter gelesen. 
Die zurückgegebene Variable kann dann entweder direkt ausgegeben oder gespeichert werden.
Hier ein Beispiel:
'''

def addition3(zahl):
  return zahl + 3
  print("Dies wir nicht ausgegeben, da es in der Zeile unter dem return steht.")
  
nummer = 34
volls_addition = addition3(nummer) + 3
print(volls_addition)

'''
Aufgabe: Schreibe ein Programm, welches eine Zahl durch Eingabe des Benutzers annimmt und diese an eine Funktion übergibt. Die Funktion soll die Zahl quadrieren und das Ergebnis dessen zurückgeben. Nach der Rückgabe soll das Ergebnis ausgegeben werden.
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############
