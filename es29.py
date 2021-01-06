#programma che chiede di inserire il nome di determinate città e di selezionare un valore massimo di escursione termica a piacere (per ognuna sarà diverso)
#successivamente chiede il valore massimo e minimo di temperatura della giornata di oggi della città. Terminato il ciclo comunica i vari risultati
print ("digita stop per terminare il ciclo e ricevere il risultato finale ")
lista_nomi_città = []
lista_esc_term = []
lista_esc_term_pred = []
contatore = 0



while True:

    nomi_città = input("inserire nome città ")
    
    if nomi_città == "stop" :
        break
    
    escursione_termica = int(input("Definisci il massimo valore che vuoi prestabilire all' escursione termica della città in questione "))
    

    temp_max_2 = int(input("digitare la temperatura massima della giornata di oggi della città "))
    temp_min_2 = int(input("digitare la temperatura minima della giornata di oggi della città "))
    escursione_termica_2 = (temp_max_2 - temp_min_2)
    
    
    if escursione_termica < escursione_termica_2 :
        contatore += 1
    else:
        pass
    

    
    lista_nomi_città.append(nomi_città)
    lista_esc_term.append(escursione_termica_2)
    lista_esc_term_pred.append(escursione_termica)
    
print ("le città che hanno avuto un'escursione termica maggiore rispetto alla prefissata sono", contatore)
print("lista delle città:", lista_nomi_città)
print("escursioni termiche per ogni città:", lista_esc_term)
print("escursione termica massima stabilita per ogni città:", lista_esc_term_pred)