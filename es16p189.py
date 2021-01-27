#programma con nazioni e capitali corrispondenti che chiede all' utente di inserire per l' appunto una nazione per sapere la rispettiva capitale CON DEF E DICT
def def_dizionario(nazioni, capitali, dizionario={}):
    for i in range(len(nazioni)):
        dizionario[nazioni[i]] = capitali[i]
    return dizionario

def main():
    nazioni = ["Italia", "Portogallo", "Germania", "Spagna", "Albania", "Repubblica Ceca", "Belgio", "Svizzera", "Svezia", "Croazia"]
    capitali = ["Roma", "Lisbona", "Berlino", "Madrid", "Tirana", "Praga", "Bruxelles", "Berna", "Stoccolma", "Zagabria"]
    dizionario1 = def_dizionario(nazioni, capitali)
    while True:
        richiesta_nazione = input("Inserire il nome di una nazione per ricevere il nome della sua capitale: ")
        richiesta_nazione = richiesta_nazione.capitalize()
        if richiesta_nazione not in dizionario1:
            stop = input("La nazione non è presente, premi 0 per fermare il ciclo o qualunque altro tasto per continuare")
            if stop == "0":
                break
        else:
            capitale = dizionario1.get(richiesta_nazione)
            stop2 = input("La capitale è:", capitale, "premi 0 per fermare il ciclo o qualunque altro tasto per continuare")
            if stop2 == "0":
                break
main()
