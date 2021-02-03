#programma inverso del precedente che chiede capitali e restituisce nazioni
def def_dizionario(nazioni, capitali, dizionario={}):
    for i in range(len(nazioni)):
        dizionario[capitali[i]] = nazioni[i]
    return dizionario

def main():
    nazioni = ["Italia", "Portogallo", "Germania", "Spagna", "Albania", "Repubblica Ceca", "Belgio", "Svizzera", "Svezia", "Croazia"]
    capitali = ["Roma", "Lisbona", "Berlino", "Madrid", "Tirana", "Praga", "Bruxelles", "Berna", "Stoccolma", "Zagabria"]
    dizionario_nazioni_capitali = def_dizionario(nazioni, capitali)
    while True:
        richiesta_capitale = input("Inserire il nome di una capitale per ricevere il nome della sua nazione: ")
        richiesta_capitale = richiesta_capitale.capitalize()
        if richiesta_capitale not in dizionario_nazioni_capitali:
            stop = input("La capitale non è presente. Premi 0 fermare il ciclo o qualunque altro tasto per continuare: ")
            if stop == "0":
                break
        else:
            nazione_corrispondente = dizionario_nazioni_capitali.get(richiesta_capitale)
            print("La nazione è:", nazione_corrispondente, "Premi 0 per fermare il ciclo o qualunque altro tasto per reimpostare la capitale:")
            stop2 = input()
            if stop2 == "0":
                break

main()