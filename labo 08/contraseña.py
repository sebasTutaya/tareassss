import random
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""

    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.islower() for c in contrasena) and
            any(c.isupper() for c in contrasena) and
            any(c.isdigit() for c in contrasena) and
            any(c in string.punctuation for c in contrasena)):
            break

    return contrasena

# Solicitar longitud de contraseña
longitud = int(input("Ingrese la longitud deseada de la contraseña: "))

# Generar y mostrar la contraseña
contrasena_segura = generar_contrasena(longitud)
print(f"Contraseña segura generada: {contrasena_segura}")

