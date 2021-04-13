print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#Hier lernen wir wie man mit Listen arbeitet

'''
Man kann Listen in Python nutzen um Elemente beliebiger Datentypen geordnet zu verstauen. Anhand des Listenplatzes kann man wieder auf die einzelnen Elemente der Liste zugreifen und diese verändern oder löschen. 
Hier ein Beispiel:
'''
studium = ["Maschinenbau","Bachelor",9,6]
'''
Wie hier schon zu sehen, kann man eine Liste durch einen Namen der Liste und dann eckige Klammern mit den Elementen darin anlegen. Um dann wieder auf die Elemente zuzugreifen wird die Stelle in der Liste, in welcher das Element steht, in Kombination mit dem Namen der Liste angegeben (Listenname[Stelle]). Es ist dabei zu beachten, dass das erste Element einer Liste an der Stelle 0 (nicht 1!) steht.
'''
print("Stelle 0: " + studium[0])
print("Stelle 1: " + studium[1])
'''
Wenn man eine längere Liste hat und auf eines der hinteren Elemente zugreifen möchte, so kann man auch von hinten auf die Liste zugreifen. Dazu werden negative Stellenangaben genutzt, dabei ist es wichtig zu wissen, dass [-1] das letzte Element ist.
'''
print("Stelle -1: " + str(studium[-1]))
print("Stelle -2: " + str(studium[-2]))
'''
Um die ganze Liste auszugeben kann der Listenname einfach in einen print Befehl geschrieben werden. Soll nur ein Element ausgegeben werden, so muss die Stelle des Elements mit angegeben werden. 
'''
print(studium)
'''
Wenn man ein Element einer Liste über die Stelle in der Liste aufruft, so kann dieses wie jede andere Variable genutzt werden. 
'''
studium[1]="Master"
print("Neuer Wert der Stelle 1: " + studium[1])
'''
Nützlich ist auch oft das Bestimmen der Anzahl der Elemente in einer Liste mit der Funktion len(Listenname).
'''
print("Die Liste Studium hat " + str(len(studium)) + " Elemente")
'''
Man kann auch nachträglich noch Elemente an eine Liste anhängen dazu wird ".append()" genutzt
'''
studium.append("Abschluss")
print(studium)
'''
Aufgabe: 
Erstelle eine Liste welche eine Einkaufsliste enthält. Fülle die Liste abwechselnd mit dem Lebensmittel welches gekauft werden soll und im nächsten Element der Anzahl dessen. Schreibe mindestens drei Lebensmittel auf die Einkaufsliste.
Ändere nun nachträglich ein Lebensmittel und die Anzahl davon. 
Für die Ausgabe soll eine Funktion geschrieben werden, die das Lebensmittel und die Anzahl annimmt und diese in der Form Anzahl x Lebensmittel ausgibt. Gebe so nach und nach die ganze Liste aus.
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############
