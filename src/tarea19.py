numero = int(input("Ingresa un número para verificar si es primo: "))
if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")