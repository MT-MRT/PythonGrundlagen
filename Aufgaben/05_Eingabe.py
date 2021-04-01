#Hier lernen wir wie wir Eingaben in dem Programm verarbeiten

'''
Eingaben werden mit dem Befehl input initiiert. Die Eingabe speichert man dann in einer Variablen ab.
Der Nutzer kann gibt dann sobald die Eingebeauffoderung kommt das gewünschte ein und bestätigt dies mit Enter.

Zum Beispiel so:
'''
eingabe_zahl = input("Gebe hier die Zahl ein: ")
eingabe_tier = input("Gebe hier den Namen eines Tieres ein: ")
print("Ein/e " + eingabe_tier + " hat " + eingabe_zahl + " Beine.\n") 

'''
Aufgabe: Erstelle eine Art kleinen Taschenrechner, welcher die ersten beiden Zahlen die der Nutzer eingibt addiert und die darauffolgenden Zahlen dividiert. Danach sollen die Ergebnisse ausgegeben werden. 

Notiz: Wichtig ist zu wissen, dass alle Eingaben als strings abgespeichert werden. Wenn du nun also versuchst die Zahlen zu addieren, wird es die Zahlen nur hinereinaderreihen, da ein plus auch zum Zusammenfügen von strings genutzt werden kann. 

Somit musst du der Eingabe einen für Zahlen adäquaten Datentyp zuweisen, wie z.B int oder wenn du auch Kommazahlen verrechen magst float (z.B int( input ("...")) ). Danach darfst du nicht vergessen bei der Ausgabe wieder eine string daraus zu machen.

Falls dich das Beispiel stört kommentier es einfach aus! (# oder ''' ''')
'''
