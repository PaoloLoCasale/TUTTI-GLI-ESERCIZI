'''
PAGINA 191 
TESTO: Risolvi la seguente variante del problema della Gestione delle lavorazioni del Coding di pag. 144.
Scrivi il programma per una macchina che accetti lavorazioni con un codice identificativo di tipo stringa:
al momento dell'inserimento di un nuovo codice occorre specificare anche la priorità della lavorazione
che può essere uguale a 0 (urgente), 1 (priorità alta) e 2 (priorità bassa), Ci sono due code di attesa: una
per l'alta priorità e una per la bassa priorità. Se la priorità è 0 il codice della lavorazione viene inserito
all'inizio della coda ad alta priorità, se la priorità è 1 il codice della lavorazione è inserito alla fine della
coda ad alta priorità e, infine, se la priorità è 2, il codice è inserito alla fine della coda a bassa priorità.
Quando la macchina termina una lavorazione, manda in esecuzione la lavorazione che si trova intesta a
una coda ottenuta dall'accodamento della coda a bassa priorità di seguito a quella di priorità alta. (GC)
'''
coda_urgente = []
coda_non_urgente = []
lista_operazioni = [1, 2, 3, 4]

def menu():
    print("--------------------------")
    print("1. Accomodamento nuova lavorazione")
    print("2. Esecuzione di una lavorazione")
    print("3. Visualizza coda lavorazioni")
    print("4. Fine lavoro")
    print("--------------------------")

def scegli_opzione():
    while True:
        scelta_opzione = int(input("Inserisci la tua scelta: "))
        while scelta_opzione not in lista_operazioni:
            print("Riprova, inserisci un valore da 1 a 4.")
            scelta_opzione = input()
        break
    return scelta_opzione

def accoda():
    while True:
        codlav = input("Inserire codice lavorazione: ")
        indice_priorita = int(input("Definire l'indice di priorità: 0, 1, 2. "))
        if indice_priorita == 0:
            coda_urgente.insert(0, codlav)
            break
        elif indice_priorita == 1:
            coda_urgente.insert(-1, codlav)
            break
        elif indice_priorita == 2:
            coda_non_urgente.append(codlav)
            break
        else:
            print("Errore, riprova: inserisci un valore da 0 a 2.")

def esegui():
    if len(coda_urgente) == 0 and len(coda_non_urgente) == 0:
        print("Code lavorazioni vuote")
    else:
        while len(coda_urgente) != 0:
            lavoro_AP = coda_urgente.pop(0)
            print("Avvio lavorazione:", lavoro_AP)
        print("Coda urgente: vuota. Avvio lavorazioni della coda non urgente...")
        while len(coda_non_urgente) != 0:
            lavoro_BP = coda_non_urgente.pop(0)
            print("Avvio lavorazione: ", lavoro_BP)

def visualizza():
    for i in range(len(coda_urgente)):
        codlav_AP = coda_urgente[i]
        print("Codice lavorazione urgente: ", codlav_AP)
    for e in range(len(coda_non_urgente)):
        codlav_BP = coda_non_urgente[e]
        print("Codice lavorazione non urgente: ", codlav_BP)

def main():
    while True:
        menu()
        scelta = scegli_opzione()
        if scelta == 1:
            accoda()
        elif scelta == 2:
            esegui()
        elif scelta == 3:
            visualizza()
        else:
            print("Fine lavoro")
            break

main()