print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############
import time
import random
zufallszahl= random.randint(2, 7)
print("Die Zufallszahl ist: " + str(zufallszahl))
for i in range(1,zufallszahl+1):
  print("Durchlauf:" + str(i))
  time.sleep(3)
  print("Diese Ausgabe ist 3 Sekunden verzögert")
