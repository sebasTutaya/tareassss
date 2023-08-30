def es_palindromo(frase):
    frase_1 = "".join(caracter.lower() for caracter in frase if caracter.isalnum())
    
    return frase_1 == frase_1[::-1]

# Ejemplo de uso
frase = "La moral, claro, mal."
if es_palindromo(frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
