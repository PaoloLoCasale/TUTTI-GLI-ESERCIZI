#Programma che ti chiede un numero in input e ti da output pari o dispari
numero = int(input("Inserisci un numero per verifica se esso sia pari o dispari "))
if numero % 2 == 0:
    print("Il numero",numero,"è pari ")
else:
    print("Il numero",numero,"è dispari ")
