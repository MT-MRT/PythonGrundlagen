print('\n\033[92m##### Tutorial #####\033[0m\n')
############## Beschreibung ##############

#In dieser Aufgabe geht es um das if else Statement

'''
Das if Statement kann man zu einem else Statement erweitern. Das else ohne eine weitere Bedinung tritt dann in Kraft, wenn die Bedingung des if Statements nicht wahr ist. Knüpft man das else an eine weitere Bedingung, so wird dafür der Befehl "elif" genutzt, so kann man Fallunterscheidungen mit mehr als einem Fall erstellen.

So erweitern wir das Bespiel um einen weiteren Fall. Nämlich ob die Zahl größer 20 ist und wenn was passiert, ween keine dieser Bedinungen eintritt. 
'''
print("Gib hier eine beliebige Zahl ein:")
zahl = int(input())

if zahl>10 and zahl<=20:
  print("Die eingegebene Zahl " + str(zahl) + " ist größer als 10.")
elif zahl>20:
  print("Die eingegebene Zahl " + str(zahl) + " ist größer als 20.")
else: 
  print("Die eingegebene Zahl " + str(zahl) + " ist kleiner oder gleich als 10.")

'''
In dem Beispiel wurde auch noch etwas Neues eingeführt. Die Verknüfung von zwei Bedingungen mit "and". Dies ist ein sogenannter logischer Operator. Mit den logischen Operatoren "and" und "or" kann man Elementarvergleiche verknüpfen.
and:
Dies ist die und-Verknüpung. Ist einer der Beiden oder beide Elementarvergleiche die daran geknüpft sind falsch, so ist die ganze Bedingung falsch. Erst wenn beide damit verknüpften Vergleiche wahr sind ist die ganze Bedingung wahr. 
or:
Dies ist die oder-Verknüpung. Ist einer der Beiden oder beide Elementarvergleiche die daran geknüpft sind wahr, so ist die ganze Bedingung wahr. Erst wenn beide damit verknüpften Vergleiche falsch sind ist die ganze Bedingung falsch. 

Aufgabe: Schreibe ein if-else Statment, welches prüft ob eine Zahl durch zwei und durch drei ohne Rest teilbar ist. Mit einem elseif soll zudem noch überprüft werden, ob die Zahl durch fünf ohne Rest teilbar ist. Trifft beides nicht zu soll mit else ein kurzer Satz der dies darlegt ausgegeben werden.
'''
print('\n\033[92m##### Lösung Studierende #####\033[0m\n')
############## Ab hier kannst du deine Lösung schreiben ##############
