def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)
palabra1 = input("Escribe la primera palabra: ")
palabra2 = input("Escribe la segunda palabra: ")
if son_anagramas(palabra1, palabra2):
    print(f'"{palabra1}" y "{palabra2}" son anagramas.')
else:
    print(f'"{palabra1}" y "{palabra2}" no son anagramas.')