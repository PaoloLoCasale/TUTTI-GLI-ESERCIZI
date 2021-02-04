#Programma che preso un dizionario di studenti e voti restituisca un altro dizionario con studenti e medie valori

import math
print("I voti vanno da 18 a 30.")

l_nomi = []
l_media_voti = []

diz = {}

k1 = range(18, 23)
k2 = range(24, 26)
k3 = range(27,30)

while True:
    nome = input("Inserire i nomi degli studenti, digitare stop per smettere:\n")
    nome = nome.capitalize()

    if nome == "Stop":
        break
    l_nomi.append(nome)

    media_voto = 0
    l_voti = []

    print("Inserire voti dello studente. Premere 0 per smettere:")

    while True:
        voto = int(input())
        if voto == 0:
            break
        l_voti.append(voto)

    for i in range(len(l_voti)):
        media_voto += l_voti[i]

    media_voto /= len(l_voti)
    
    lode = input("Lo studente ha una lode? ")
    lode = lode.upper()
    if lode == "SI":
        media_voto = round(media_voto, 0)
    else:
        media_voto = math.trunc(media_voto)
    
    l_media_voti.append(media_voto)

    for e in range(len(l_nomi)):
        diz[l_nomi[e]] = l_media_voti[e]
    

def dizionario(l1 = [], l2 = [], l3 = []):

    d_finale = {
        k1 : l1,
        k2 : l2,
        k3 : l3
    }
    
    for i in range(len(l_nomi)):
        if l_media_voti[i] >= 18 and l_media_voti[i] <= 23:
            l1.append(l_nomi[i])
        elif l_media_voti[i] >= 24 and l_media_voti[i] <= 26:
            l2.append(l_nomi[i])
        elif l_media_voti[i] >= 27 and l_media_voti[i] <= 30:
            l3.append(l_nomi[i])
        else:
            print(media_voto)
            print("Media voti di", l_nomi[i], "non compatibile con i range.")
    return d_finale

d = dizionario()
print(d)
    

