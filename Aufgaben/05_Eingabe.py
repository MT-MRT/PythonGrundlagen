print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#Hier lernen wir wie man Nutzeringaben in einem Programm verarbeitet

'''
Nutzereingaben werden mit dem Befehl input initiiert. Die Eingabe wird dann in einer Variablen abgespeichert.
Der Nutzer gibt dann sobald die Eingebeauffoderung kommt seine Eingabe ein und bestätigt dies durch das Drücken der Entertaste.
Zum Beispiel so:
'''
eingabe_zahl = input("Gebe hier die Zahl ein: ")
eingabe_tier = input("Gebe hier den Namen eines Tieres ein: ")
print("Ein/e " + eingabe_tier + " hat " + eingabe_zahl + " Beine.\n") 

'''
Aufgabe: Erstelle eine Art kleinen Taschenrechner, welcher die ersten beiden Zahlen die der Nutzer eingibt addiert und die darauffolgenden Zahlen dividiert. Danach sollen die Ergebnisse ausgegeben werden. 
'''
# Notiz: Wichtig ist zu wissen, dass alle Eingaben als strings abgespeichert werden. Wenn du nun also versuchst die Zahlen zu addieren, wird es die Zahlen nur hinereinaderreihen, da ein Plus auch zum Zusammenfügen von Strings genutzt werden kann. Somit musst man der Eingabe einen adäquaten Datentyp zuweisen, wie z.B int oder wenn man auch Kommazahlen rechnen möchte float (z.B int(input("...")) ). Danach darfst man jedoch nicht vergessen bei der Ausgabe wieder eine String daraus zu machen.
# Falls dich das Beispiel stört kommentier es einfach aus! (#.... oder ''' ... ''')

print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############
