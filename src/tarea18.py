numero_limite = int(input("Escribe un número para generar la serie de Fibonacci hasta ese valor: "))
a, b = 0, 1
serie_fibonacci = []
while a <= numero_limite:
    serie_fibonacci.append(a)
    a, b = b, a + b
print(f"Serie de Fibonacci hasta {numero_limite}: {serie_fibonacci}")