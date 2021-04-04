print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############

def ausgabe(lebensmittel, anzahl):
  print(str(anzahl) +" x "+ str(lebensmittel))

einkauf=["Banane",2,"Brot",1,"Öl",1,"Nudeln",2]
einkauf[4]="Gurke"
einkauf[5]= 2
print(str(len(einkauf)) + " Dinge müssen gekauft werden")
ausgabe(einkauf[0],einkauf[1])
ausgabe(einkauf[2],einkauf[3])
ausgabe(einkauf[4],einkauf[5])
ausgabe(einkauf[6],einkauf[7])
