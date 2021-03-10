'''
ES 5: elenca proprietà e metodi della classe prodotto.
ES 6: definisci il metodo assegna_prezzo della classe prodotto.
'''

class Prodotto():
    def __init__(self,interni, macchina):
      
        self.interni = interni
        self.macchina= macchina
    def assegna_prezzo(self):
        diz_macchina = {
            1: "Ferrari",
            2: "Cadillac",
            3: "Dacia",
            4: "Fiat Panda 4x4"
        }  

        diz_interni = {
            1: "interni standard",
            2: "interni auto da corsa",
            3: "interni di lusso, full optional"
        }

        try:
            macchina = list(diz_macchina.values())[self.macchina-1]
            prezzo_macchina = 0
            
            if macchina in diz_macchina.values():
                if macchina == "Ferrari":
                    prezzo_macchina += 200
                elif macchina == "Cadillac":
                    prezzo_macchina += 80
                elif macchina == "Dacia":
                    prezzo_macchina += 20
                else:
                    prezzo_macchina += 10
            
               
                interni_macchina = list(diz_interni.values())[self.interni-1]

                try:
                    if interni_macchina in diz_interni.values():
                        if interni_macchina == "interni standard":
                            prezzo_macchina += 10
                        elif interni_macchina == "interni auto da corsa":
                            prezzo_macchina += 20
                        else:
                            prezzo_macchina += 80
                except:
                    print("Errore. ")
            
                return prezzo_macchina
        except:
            print("Errore. ")

        
def main():
    print("\n|------------------|\nBenvenuto al concessionario, quale macchina vuoi comprare? \n INSERISCI IL NUMERO CHE AFFIANCA IL NOME DELLA MACCHINA")
    print("------------------\n1: Ferrari\
        \n2: Cadillac\
        \n3: Dacia\
        \n4: Fiat Panda 4x4\n------------------")

    macchina_da_comprare = int(input())
   

    print("------------------\nLista interni:\
        \n1: interni standard\
        \n2: interni auto da corsa\
        \n3: interni di lusso + full optional\n------------------ ")
    
    interni = int(input("Con quali interni vuoi la macchina? \nScrivi il numero dell' interno che preferisci.\n------------------\n"))

    spesa_totale = Prodotto(interni, macchina_da_comprare)
    conto = spesa_totale.assegna_prezzo()

    if conto != None:
        print("Costo totale della macchina:", conto,"mila euro")
        print("|------------------|")
    else:
        print("|------------------|")


main()