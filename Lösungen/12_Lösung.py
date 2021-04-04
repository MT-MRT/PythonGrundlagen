print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############
namen=["Tom", "Tina", "Simone", "Ted", "Charlie"]

print("Erste Ausgabe:")
for person in namen:
  print(person)

länge=len(namen)

print("\nZweite Ausgabe:")
for j in range(0, länge):
  print(str(j+1) +". "+ namen[j])
