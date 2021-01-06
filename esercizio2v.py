#programma che comunica in modo casuale gli stipendi di 5 diversi dipendenti e ne calcola la media
from random import randint
print("ecco la gli stipendi e la loro media dei dipendenti a, b, c, d, e,")
while True:
    stipendioa = randint(1500, 3000)
    stipendiob = randint(1500, 3000)
    stipendioc = randint(1500, 3000)
    stipendiod = randint(1500, 3000)
    stipendioe = randint(1500, 3000)
    print("Gli stipendi di ciascun dipendente sono",stipendioa,stipendiob, stipendioc, stipendiod, stipendioe)
    mediastipendi = ((stipendioa + stipendiob + stipendioc + stipendiod + stipendioe)/5)
    print("La media corrisponde a",mediastipendi)
    break
    