#ES 25: Classe di 30 studenti con chiave matricola e valore voto.  Elencare risultati e visualizzare tipi di voto diversi (scrivendo solo 1 volta i voti uguali)
#ES 26: Con il dizionario precedente, vengono elencati i numeri di matricola delle persone con voti superiori alla media di tutte le valutazioni

import statistics

matricola = 0
lista_matricole = []
lista_voti = []
tipi_di_voti = []
matricola_sopra_media = []
dizionario_matricole_voti = {}

for i in range(30):
    matricola += 1
    print("Inserire voto della matricola", matricola, "nel registro: ")
    voto = int(input())
    lista_matricole.append(matricola)
    lista_voti.append(voto)

for o in range(len(lista_matricole)):
    dizionario_matricole_voti[lista_matricole[o]] = lista_voti[o]

for a in range(len(lista_matricole)):
    if lista_voti[a] not in tipi_di_voti:
       tipi_di_voti.append(lista_voti[a])
    else:
        pass

def media(contatore_matricole = 0):
    media_voti = statistics.mean(lista_voti)
    for e in range(len(lista_matricole)):
        contatore_matricole += 1
        if lista_voti[e] > media_voti:
            matricola_sopra_media.append(lista_matricole[contatore_matricole-1])
    print("La media dei voti corrisponde a: ", media_voti)
    return matricola_sopra_media

tipi_di_voti.sort()
print("Dizionario matricole e voti corrispondenti: ", dizionario_matricole_voti)
print("Tipi di voti: ", tipi_di_voti)
print("Le matricole sopra la media sono: ", media()) 
    



   
  

