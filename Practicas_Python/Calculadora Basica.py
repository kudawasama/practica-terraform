# Calculadora básica en Python# Esta calculadora permite realizar operaciones básicas: suma, resta, multiplicación y división.
# El usuario puede ingresar dos números y un símbolo para realizar la operación.   
# Si el usuario ingresa 'salir' en el primer número, el programa termina.
# Si el usuario ingresa un símbolo no válido o números no válidos, se muestra un mensaje de error y se solicita nuevamente la entrada.


while True:




    print("====Calculadora simple======")
    print("Ingrese 'salir' para terminar el programa")  

    print("Ingrese dos números y un símbolo para realizar una operación")
    print("Símbolos disponibles: +, -, *, /")   
    print("Para salir, escriba 'salir' en el primer número")
    input_num = input("Ingrese el primer número: ")
    if input_num.lower() == 'salir':
        print("Programa terminado.")
        break  
    simbolo = input("Ingrese el símbolo de la operación: ")
    num_2 = input("Ingrese el segundo número: ")   
    try:
        num_1 = float(input_num)
        num_2 = float(num_2)
    except ValueError:
        print("Error: Entrada no válida. Asegúrese de ingresar números válidos.")
        continue   
    if simbolo not in ["+", "-", "*", "/"]:
        print("Error: Símbolo no válido. Use +, -, * o /.")
        continue
    resultado = None
    # Realizar la operación según el símbolo ingresado

    print(f"Realizando la operación: {num_1} {simbolo} {num_2}")
    if simbolo == "+":
        resultado = num_1 + num_2
    elif simbolo == "-":
        resultado = num_1 - num_2
    elif simbolo == "*":
        resultado = num_1 * num_2
    elif simbolo == "/":
        if num_2 == 0:
            print("Error: División por cero no permitida.")
            continue
        resultado = num_1 / num_2
    print(f"El resultado de {num_1} {simbolo} {num_2} es: {resultado}")
    print("================================")
    
    



    

