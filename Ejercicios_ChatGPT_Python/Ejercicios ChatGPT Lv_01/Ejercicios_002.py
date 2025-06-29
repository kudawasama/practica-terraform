"""numero par o impar"""
# Pregunta un número y dice si es par o impar

print("Introduce un número: ")
numero = int(input()) 
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

    