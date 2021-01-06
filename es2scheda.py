#programma che chiede di inserire un numero qualsiasi di parole e ne conta le lettere
lista_a = []
lista_b = []
parole = input("Digita le parole che vuoi che vengano analizzate ")
lista_a.append(parole)
lunghezza_parole = len(lista_a)
for numero_lettere in range(lunghezza_parole):
    lunghezza_b = len(lista_a[numero_lettere])
    lista_b.append(lunghezza_b)
print("Il numero di lettere delle parole è",lista_b)
    
