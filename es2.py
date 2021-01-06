#Esercizio 26
#Programma che chiede di inserire gli stipendi di un tot di dipendenti e poi ne fa la media
lista_stipendi = []
conteggio = True
dipendente = 0
ripetizioni = 0
somma = 0
while conteggio == True:
    dipendente += 1
    ripetizioni += 1
    print("Stipendio dipendente", dipendente,"? ")
    stipendi_dipendente = int(input())
    lista_stipendi.append(stipendi_dipendente)

    if ripetizioni == 5:
        tasto_premuto = int(input("se vuoi fermare qui il conteggio e osservare la media degli stipendi, premi -1, in caso contrario premi 0 "))
        ripetizioni = 0
        if tasto_premuto == -1:
            conteggio = False
        else:
            pass
for x in lista_stipendi:
    somma += x
lista1 = len(lista_stipendi)
print(lista_stipendi)
mediastipendi = somma/lista1
print(mediastipendi)
