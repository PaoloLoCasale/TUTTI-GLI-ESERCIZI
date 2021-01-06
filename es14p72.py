#programma che chiede due valori, se moltiplicati tra loro danno un ris. maggiore di 10, il programma attua una differenza, in caso contrario una somma
a = int(input("Inserire valore a "))
b = int(input("Inserire valore b "))
if a*b > 10:
    print("La differenza tra i due numeri risulta:",a-b)
else:
    print("La somma tra i due numeri risulta:",a+b)
