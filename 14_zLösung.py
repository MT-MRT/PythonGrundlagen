import random

def mittelwert(zahl1, zahl2, zahl3):
  mittelwert = (zahl1 + zahl2 + zahl3)/3
  return mittelwert

def ausgabe(eingabe,info):
  print(str(eingabe) + " " + info)

print("Lösung:")

zahl1 = float(input("Gebe hier die erste Zahl ein: "))
zahl2 = float(input("Gebe hier die zweite Zahl ein: "))
zahl3 = float(input("Gebe hier die dritte Zahl ein: "))

mittelwert_zahl=mittelwert(zahl1, zahl2, zahl3,)
ausgabe(mittelwert_zahl, "Mittelwert")
zufallszahl= random.randint(1, 100000)  
ausgabe(zufallszahl, "Zufallszahl")

fläche = mittelwert_zahl*zufallszahl
ausgabe(fläche, "m^2 - Fläche")

if fläche>=1000000:
  fläche = fläche/1000000
  ausgabe(fläche, "km^2 - Fläche") 
