#In diesem Abschnitt wird die Benutzung von Funktionen erklärt

'''
Mit Funktionen bringen wir Struktur in unseren Code und können Programmabfolgen die mehrmals vorkommen zusammenfassen und somit den Code zu verkürzen und Fehler vermeinden.

Hier ein Beispiel einer Funktion:
'''

def halloWelt():
  print("Hallo Welt!")

print("Anfang des Programms")
halloWelt()
halloWelt()
print("Ende des Programms")

'''
Wie man hier schon sieht wird eine Funktion wird mit dem Keyword "def" eingeführt und mit einem Namen benannt. Danach stehen Klammern die im Moment noch leer sind, aber in der nächsten Aufgabe werden diese mit Variablen gefüllt. Zum Abschluss der Zeile steht ein Doppelpunkt, in der nächsten Zeile beginnt dann der Programmcode der Funktion.

Alle Codezeilen die zu dieser Funktion gehören sind eingerückt. Der Einschub hat den gleichen Zweck wie die geschweiften Klammern in Java, sie zeigen dem Compiler wo der Anfang und das Ende der Funktion sind.

Alles was dann in der Funktion steht wird immer dann abgerufen sobald die Funktion mithilfe ihres Namens im Programm aufgerufen wird. Somit wird das Programm nicht wie zuvor von oben nach unten stumpf abgearbeitet. Die Funktion die zwar ganz oben definiert ist wird erst nachdem sie aufgerufen wurde umgesetzt.

Aufgabe: Schreibe zwei Funktionen welche beide nur einen Ausgabebefehl enthalten. Rufe diese dann zweimal hintereinander abwechselnd auf. 
'''
