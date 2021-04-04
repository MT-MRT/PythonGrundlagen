print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############

zahl = 0
geradeZahlen = [0,0,0,0]
i = 0

while i < 4:

    zahl = int(input("Gebe bitte eine gerade Zahl ein: "))

    if zahl % 2 != 0:
        print("Diese Zahl ist nicht gerade!")

    else:
     geradeZahlen[i]=zahl
     i+=1

    print("\n" + str(geradeZahlen) + "\n")
