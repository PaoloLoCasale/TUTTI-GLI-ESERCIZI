

def voti(elenco = {}, stop=0):
    while stop == 0:
        nome = input("Inserisci nome studente, se hai finito premi stop")
        if nome == "Stop":
            elenco[nome] = voti_tot
            print(elenco)
            break
        else:
            voto_1 = int(input("Inserire voto 1"))
            voto_2 = int(input("Inserire voto 2"))
            voto_3 = int(input("Inserire voto 3"))
            voti_tot = (voto_1, voto_2, voto_3)
            media_voti = ((voto_1+voto_2+voto_3)/3)
            print("I voti di",nome,"sono",voto_1, voto_2, voto_3,"La loro media è",media_voti)
    
        

voti()

 





        

        
        
        
    
   




