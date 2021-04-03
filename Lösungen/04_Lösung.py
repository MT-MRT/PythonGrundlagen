print('\n\033[92m##### Lösung #####\033[0m\n')
############## Mögliche Lösung ##############

nummer4 = 45
nummer5 = nummer4 - 5
print("nummer4:" + str(nummer4))
print("nummer5:" + str(nummer5))
print(max(nummer4, nummer5 + 7)) 
print("nummer4:" + str(nummer4))
print("nummer5:" + str(nummer5))
print("Dir sollte auffallen, das mit dem Addieren von 7 zu nummer5, innerhalb der print Operation, der Wert der eigentlichen Variable nicht verändert wird. Den Wert der Variable an sich würde man z.B so verändern: ")
nummer4 = 45
nummer5 = nummer4 - 5
print("nummer4:" + str(nummer4))
print("nummer5:" + str(nummer5))
nummer5 = nummer5 + 7 # oder kürzer nummer5 += 7
print(max(nummer4, nummer5)) 
print("nummer4:" + str(nummer4))
print("nummer5:" + str(nummer5))
