"""Sumar todos los números del 1 al 100"""  
# Muestra la suma total con un bucle


while True:
    try:
        suma = 0
        for numero in range(1, 101):
            suma += numero
        print(f"La suma de los números del 1 al 100 es: {suma}")
        break
    except Exception as e:
        print(f"Error: {e}. Inténtalo de nuevo.")
        
        
