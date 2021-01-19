#programma che chiede valori variabili a,b,c 
#li usa x calcolare il fuoco e il vertice di una parabola

def delta(a,b,c):
    delta = (b*b - 4*a*c)
    return delta
def fuoco(a,b,c):
    delta_fuoco = delta(a,b,c)
    x_fuoco = (-b/2*a)
    y_fuoco = (1-delta_fuoco/4*a)
    return x_fuoco, y_fuoco
def vertice(a,b,c):
    delta_vertice = delta(a,b,c)
    x_vertice = (-b/2*a)
    y_vertice = (-delta_vertice/4*a)
    return x_vertice,y_vertice

def main():
    a = int(input("Definisci a" ))
    b = int(input("Definisci b" ))
    c = int(input("Definisci c" ))
    coordinate_fuoco = fuoco(a,b,c)
    coordinate_vertice = vertice(a,b,c)
    print("coordinate fuoco:", coordinate_fuoco,
          "coordinate vertice:", coordinate_vertice)

main()

