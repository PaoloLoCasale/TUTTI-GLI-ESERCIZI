#Crea una rubrica con nomi persone e corrispettivi numeri telefonici. Fornito successivamente il nome della persona, il programma visualizzerà il suo numero

lista_numeri = []
lista_nomi = []
dizionario_nomi_numeri = {}

while True:
    nome = input("Inserire il nome della persona: ")
    print("inserire il numero telefonico di", nome, ":")
    numero = input()
    
    lista_nomi.append(nome)
    lista_numeri.append(numero)

    print("Digita un qualsiasi tasto non numerico per continuare a inserire persone con il loro numero. Premi stop per terminare il ciclo e visualizzare la rubrica. ")
    stop = (input())
    if stop == "stop":
        break

for i in range(len(lista_nomi)):
    dizionario_nomi_numeri[lista_nomi[i]] = lista_numeri[i]

print(dizionario_nomi_numeri)

while True:
    print("Digitare il nome di una persona per cercare il suo numero nella rubrica: ")
    corrispondenza_nome_numero = input()
    if corrispondenza_nome_numero in dizionario_nomi_numeri.keys():
        print(dizionario_nomi_numeri.get(corrispondenza_nome_numero))
    else:
        print(corrispondenza_nome_numero, "non è nella rubrica.")
    print("Premere un qualsiasi tasto non numerico per continuare la ricerca dei contatti nella rubrica. Premere stop per terminare. ")
    stop2 = (input())
    if stop2 == "stop":
        break