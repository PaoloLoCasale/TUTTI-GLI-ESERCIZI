#Programma che preso un dizionario di studenti e voti restituisca un altro dizionario con studenti e medie valori

import math

def main():
    
    dizionario_studenti = {"Marco":[24,28,25], "Fabio":[18,22,26],
    "Alessandro":[28,23,27]}
    print("Ecco i nomi degli studenti e l' elenco dei loro voti",dizionario_studenti)
    
    voti_marco = dizionario_studenti.get("Marco")
    media_voti_marco = ((sum(voti_marco))/3)
    voti_fabio = dizionario_studenti.get("Fabio")
    media_voti_fabio = ((sum(voti_fabio))/3)
    voti_ale = dizionario_studenti.get("Alessandro")
    media_voti_ale = ((sum(voti_ale))/3)
    
    diz_voti = {"Marco": media_voti_marco, "Fabio": media_voti_fabio, "Alessandro": media_voti_ale}
    print("Ecco la media dei voti per ogni studente",diz_voti)

main()
    

