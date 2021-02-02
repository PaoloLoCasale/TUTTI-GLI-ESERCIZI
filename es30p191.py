def registrazione_membri_coda(coda=[], stop=0):
    while stop == 0:
        registro = input("Digitare i nomi delle persone che costituiscono la coda, per fermare la registrazione premi stop: ")
        registro = registro.capitalize()
        if registro == "Stop":
            break
        else:
            coda.append(registro)
    return coda

def main():
    print("La coda è costituita da:", lista_coda)
    print("Il primo della coda,", lista_coda[0],"può entrare. ")
    while True:        
        print("Il paziente",lista_coda[0],"ha finito! ")
        lista_coda.pop(0) 
        if len(lista_coda) == 0:
            print("Coda terminata. ")
            break
        else:
            print("Ora tocca a", lista_coda[0],"Entri pure. ")

lista_coda = registrazione_membri_coda()
main()