print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############

nummer= int(input("Gib hier eine Zahl ein: "))
if nummer%2==0 and nummer%3==0:
  print("Die eingegebene Zahl " + str(nummer) +" ist durch zwei und drei ohne Rest teilbar und somit auch ohne Rest durch 6 teilbar.")
elif nummer%5==0:
  print("Die eingegebene Zahl " + str(nummer) +" ist durch fünf ohne Rest teilbar.")
else:
  print("Die eingegebene Zahl " + str(nummer) +" ist durch nicht durch 6 oder durch 5 teilbar.")
