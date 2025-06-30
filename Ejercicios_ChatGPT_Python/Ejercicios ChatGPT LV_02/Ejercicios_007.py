"""Contador del 1 al 10"""
# Usar while o for para contar hasta 10

while True:
    try:
        contador = 1
        while contador <= 10:
            print(contador)
            contador += 1
        break
    except Exception as e:
        print(f"Error: {e}. Inténtalo de nuevo.")


# Alternativa usando for  
for contador in range(1, 11):
    print(contador)
    