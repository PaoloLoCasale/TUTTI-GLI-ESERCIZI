#programma che trasforma i numeri binari in numeri decimali 
lunghezza = int(input("Digita il numero delle cifre del numero binario "))

somma_cifre = 0

for i in range (lunghezza):
    
    elenco_cifre = int(input("Digita le cifre a partire dalla destra del numero "))
    valore_num = (elenco_cifre*2**i)
    somma_cifre += valore_num

print (somma_cifre)