"""Tabla de multiplicar del número que elija el usuario"""

# Imprime del 1 al 10 multiplicado por ese número


while True:
    try:
        # Pregunta al usuario si quiere continuar
        print("¿Quieres ver la tabla de multiplicar de un número? (s/n): ")
        respuesta = input().strip().lower()
        if respuesta != 's':
            print("Saliendo del programa.")
            break
    except Exception as e:
        print(f"Error: {e}. Por favor, intenta de nuevo.")
        continue

    print("Introduce un número para ver su tabla de multiplicar: ")
    numero = int(input())   
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")  
    print("¿Quieres ver otra tabla de multiplicar? (s/n): ")
    respuesta = input().strip().lower()
    if respuesta != 's':
        print("Saliendo del programa.")
        break 
    else:
        print("Volviendo a solicitar un número para la tabla de multiplicar.")
# --- IGNORE ---





# Fin del programa
# --- IGNORE ---

