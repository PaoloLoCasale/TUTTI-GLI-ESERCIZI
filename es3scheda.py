#programma che calcola le aree di varie figure (quadrati, cerchi, rettangoli, triangoli)
while True:
    risposta_calcolo = input("Digita q per calcolare l'area del quadrato, , digita c per calcolare l'area de cerchio, digita r per calcolare l'area del rettangolo, digita t per calcolare l'area del triangolo. Per uscire digita 1 ")
    if risposta_calcolo == "q":
        lato1 = int(input("Digita la lunghezza del lato: "))
        print("L'area del quadrato è " , lato1*lato1)
    elif risposta_calcolo == "c":
        raggio_cerchio = int(input("Digita la lunghezza del raggio : "))
        print("L'area del cerchio è " , raggio_cerchio**2*3.14)
    elif risposta_calcolo == "r":
        base1 =int(input("Digita la lunghezza della base: "))
        altezza1 =int(input("Digita la lunghezza dell'altezza: "))
        print("L'area del quadrato è " , base1*altezza1)
    elif risposta_calcolo == "t":
        base2= int(input("Digita la lunghezza della base: "))
        altezza2 =int(input("Digita la lunghezza dell'altezza: "))
        print("L'area del triangolo è " , (base2*altezza2)/2)
    elif risposta_calcolo == "1":
        break
    else:
        pass



 


