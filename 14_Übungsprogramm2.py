#Dies ist ein Übungsprogramm um zu lernen die einzeln gelernten Elemente zu verknüpfen, der Fokus liegt hier auf der Nutzung von Funktionen
'''
Aufgabe:
Schreibe ein Programm das drei float Werte über die Nutzereingabe annimmt und aus diesen erst mithilfe der Funktion "mittelwert" den Mittelwert der drei Zahlen bildet. 

Das Ergebnis soll dann über eine Weitere Funktion namens "ausgabe" das Ergebnis und ein erklärendes Wort dazu ausgeben (Beispielausgabe: 345,5 - Mittelwert).

Weiterführend soll eine Zufallszahl zwischen 1 und 100000 generiert werden. Dafür muss das Modul "random" importiert werden. Zum Generieren der Zufallszahl wird dann die in random vorhandene Funktion ".randint()" genutzt, diese wird mit "random.radint()"aufgerufen. In den Klammern von radiant werden zurerst der Anfangswert und dann der Endwert der Menge, aus der die Zufallszahl generiet werden soll, übergeben (Beispiel das Erstellen eines zuälligen Würfels: würfel = random.radiant(1,6)). 

Sobald die Zufallszahl generiert wurde soll diese mit dem Mittelwert zu einer Fläche [m^2] multipliziert werden. Sowohl die generierte Zufallszahl als auch die entstandene Fläche sollen über die Funktion "ausgabe" mit Wert und einem erklärenden Wort ausgegeben werden. 

Als letztes folgt noch eine Fallunterscheidung. Wenn die berechnete Fläche größer als 1000000m^2 ist, soll sie in Quadratkilometer [km^2] umgerechnet werden und wieder über die Funktion "ausgabe" ausgegeben werden. 

Tipps:
1.Die Funktion "mittelwert" muss die drei Zahlen annehmen und den Mittelwert mithilfe von "return" zurückgeben. 
2.Die Funktion "ausgabe" muss den Wert und einen string annehmen und diese zusammen über einen String Befehl ausgeben.
3.Der import für die Zufallszahl muss ganz oben im Programm stehen. Für das importieren von Modulen muss immer das Keyword "import" von den Namen des Moduls gesetzt werden.
4. Für die Fallunterscheidung am Ende ist es am Besten ein if-Statement zu nutzen.
'''
