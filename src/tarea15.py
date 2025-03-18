numeros = list(map(int,input("Ingresa números separados por espacio: ").split()))
pares = [num for num in numeros if num % 2 == 0]
lim = int(input("Ingresa un número límite: "))
impares = [num for num in numeros if num % 2 != 0 and num <= lim]
print("Números pares:", pares)
print("Números impares hasta el límite:", impares)