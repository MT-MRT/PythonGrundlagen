print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############

i = 1
eingabe_zahl = int(input("Gebe hier die Zahl ein: "))
while i<= eingabe_zahl:
  if (eingabe_zahl%i) == 0:
    print(str(i) + " ist ein Teiler")
  else:
    print(str(i) + " ist kein Teiler")
  i +=1
print("Super! Es wurden alle Teiler von " + str(eingabe_zahl) + " gefunden")
