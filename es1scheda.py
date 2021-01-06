#programma che comunica se la parola inserita dall' utente sia palondroma o meno
parola = input("Digita la parola ")
if parola == parola[::-1] :
    print("La parola è palindroma ")
else:
    print("La parola non è palindroma ")