#programma che trasforma un numero decimale in un numero binario

num_binario = []

numero_decimale = int(input("Digita un numero decimale qualsiasi "))

while True:

    quoziente = int(numero_decimale/2)
    resto = numero_decimale%2
    
    if resto == 1:
        num_binario.append(1)
    else:
        num_binario.append(0)
    numero_decimale = quoziente
    
    if quoziente == 0:
        break

num_binario.reverse ()

print (num_binario)