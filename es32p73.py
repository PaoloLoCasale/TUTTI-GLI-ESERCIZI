#programma che risolve un equazione di primo grado (inoltre ho importato Fraction, affinchè potessi trasformare il risultato in frazione)
from fractions import Fraction
print("Risolviamo una equazione di primo grado ax + b = 0 ")
a = int(input("Inserire valore di a "))
b = int(input("Inserire valore di b "))
x = -b/a
if a == 0 and b == 0:
    print("L'equazione risulta indeterminata ")
if a == 0 and b != 0:
    print("L'equazione risulta impossibile ")
if b == 0 and a != 0:
    print("x = 0 ")
if a != 0 and b != 0:
    print("Il risultato dell' equazione è:",Fraction(x).limit_denominator())

