print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#Hier wird die Nutzung von Schleifen eingeführt

'''
Nun lernen wir wie man Schleifen nutzt. Schleifen sind sehr wichtig um bestimmte Vorgänge die mehrmals durchgefürhrt werden nicht immer erneut schreiben zu müssen, als auch um Vorgänge so lange zu wiederholen bis das erwünschte Ziel erreicht ist.
In der letzten Aufgabe hatten wir mehrmals hintereinader den Aufruf zur Ausgabe der Liste Solch eine Listenausgabe kann man mit einer for-Schleife vereinfachen.
'''
print("Erster Aufruf der Liste einkauf")
einkauf= ["Apfel", "Brot", "Chips", "Nudeln"]

for lebensmittel in einkauf:
  print(lebensmittel)

'''
Die for-Schleife geht die einzelnen Elemente der Liste bis sie zum letzten Element kommt durch und gibt diese aus. 

Eine for Schleife kann man aber auch nutzen, wenn man etwas bestimmt oft wiederholen möchte. Dazu wird eine Zählvariable, wie hier zum Beispiel i, genutzt. Diese wird jeden Schleifendurchlauf um eins erhöht. Mit range(1,5)wird angegeben bis zu welchem Wert von i die Schleife laufen soll. 
Ist die for Schleife zu Ende kann man wie bei einem if-Statement eine else anhängen welches dann in Kraft tritt.
'''
print() #dieses print ist nur für einen Absatz in der Ausgabe, damit diese übersichtlicher wird, da
for i in range(1, 5):
	print (i)
else:
	print ("Die for-Schleife ist zu Ende.")

'''
Mit dem Nutzen von der Zählvariable kann man auch die Ausgabe einer Liste gestalten: 
'''
print("\nZweiter Aufruf der Liste einkauf")
for s in range(0,len(einkauf)):
  print (einkauf[s])

''''
Aufgabe:
Schreibe eine Liste welche fünf Personennamen enthält. Zuerst soll diese Liste über die zuerst gelernte Art der Ausgabe ausgegeben werden. 
Als Zweites soll die Liste mit einer weiteren for-Schleife und der Nutzung von einer Zählvariablen nochmals ausgegeben werden. Bei dieser Ausgabe sollen die einzelnen Ausgaben zusätzlich von 1 bis 5 nummeriert werden. 
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############
