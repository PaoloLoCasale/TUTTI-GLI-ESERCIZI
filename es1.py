#Esercizio 24 e 25 (insieme)
#programma che trova le percentuali di votazione di due candidati x e y (casualmente) e che li scrive in ordine alfabetico
from random import randint
print("le percentuali dei voti dei due candidati  x e y sono:")
x = randint(1, 100)
y = (100-x)
print(x, y)

print(" lista dei candidati in ordine alfabetico: x, y")
if x > y :
    print(" lista dei candidati in ordine decrescente: x, y")
else:
    print(" lista dei candidati in ordine decrescente: y, x")