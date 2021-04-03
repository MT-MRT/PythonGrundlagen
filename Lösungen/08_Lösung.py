print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############

def rechner(zahl):
  return zahl*zahl

nummer = float( input( "Bitte gebe die Zahl ein die die quadriert werden soll: "))
print(rechner(nummer))

'''
print('\n\033[92m##### Lösung #####\033[0m\n')
############## Hier noch eine weitere mögliche Lösung, zum Anschauen einefach die  (''' ''') entfernen ##############

def rechner(zahl):
  quadrieren = zahl*zahl
  return quadrieren

zahl = float( input( "Bitte gebe die Zahl ein die die quadriert werden soll: "))
quadriert = rechner(zahl)
print(quadriert)
'''
