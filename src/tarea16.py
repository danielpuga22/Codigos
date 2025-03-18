def factorial(n):
    if n < 0:
        return "no se pueden numeros negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
numero = int(input("Ingresa un número para calcular su factorial: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")