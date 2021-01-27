#programma con nazioni e capitali corrispondenti che chiede all' utente di inserire per l' appunto una nazione per sapere la rispettiva capitale

nazioni = ["Italia", "Portogallo", "Germania", "Spagna", "Albania", "Repubblica Ceca", "Belgio", "Svizzera", "Svezia", "Croazia"]
capitali = ["Roma", "Lisbona", "Berlino", "Madrid", "Tirana", "Praga", "Bruxelles", "Berna", "Stoccolma", "Zagabria"]
while True:
    richiesta_nazione = input("Digitare il nome di una nazione per sapere la sua capitale, per fermare il ciclo premi un tasto qualsiasi ")
    richiesta_nazione = richiesta_nazione.capitalize() #per mettere la maiuscola
    if richiesta_nazione in nazioni:
        i = nazioni.index(richiesta_nazione)
        print(capitali[i])
    else:
        print(richiesta_nazione,"Non è presente nella lista, stop al ciclo")
        break
