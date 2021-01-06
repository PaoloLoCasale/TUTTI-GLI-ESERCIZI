#es28
#Programma che chiede determinati valori di lancio del peso di determinati studenti e che ne comunica il valore maggiore

print("Quando desidera che il ciclo termini, scriva: stop ")

#lista dei valori del lancio dei vari studenti
list_val = []

while True:
    
    nome_studente = input("inserire nome studente ")
    
    if nome_studente  == ("stop") :
        break
    else:
        pass
    
    valore_lancio = int(input("inserire valore lancio dello studente "))
    
    list_val.append(valore_lancio)

print("il valore più alto registrato oggi è..." )
print(max(list_val)) 
