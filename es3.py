#es27
#programma che chiede in un tot di giorni quanti veicoli sono transitati e ne fa il resoconto finale
lista_veicoli = []
conteggio = True
numerogg = 0
ripetizioni = 0
somma = 0
while conteggio == True:
    numerogg += 1
    ripetizioni += 1
    print("Quanti veicoli sono entrati il giorno", numerogg,"? ")
    veicoli = int(input())
    lista_veicoli.append(veicoli)

    if ripetizioni == 5:
        risp = int(input("se vuoi uscire e vedere quanti veicoli sono passati in questi giorni, premi 0, se vuoi continuare premi -1 : "))
        ripetizioni = 0
        if risp == 0:
            conteggio = False
        else:
            pass
for x in lista_veicoli:
    somma += x
print("In un totale di", numerogg,"giorni, sono transitati", somma, "veicoli")