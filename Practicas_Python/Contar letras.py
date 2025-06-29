#Programa para contar letras en una palabra
# Este programa solicita al usuario que ingrese una palabra y cuenta la cantidad de letras en ella



while True:
    print("====Contador de Letras======")
    print("Ingrese 'salir' para terminar el programa")
    print("Ingrese una palabra para contar sus letras")
    palabra = input("Ingrese una palabra: ") 
    if palabra.lower() == 'salir':
        print("Programa terminado.")    
        break
    if not palabra.isalpha():
        print("¡Error! Lo ingresado no es una palabra, contiene números o caracteres no permitidos.")
        continue
    cantidad_letras = len(palabra)
    print(f"La cantidad de letras en la palabra '{palabra}' es: {cantidad_letras}")


# Programa para contar letras en una palabra
# Este programa solicita al usuario que ingrese una palabra y cuenta la cantidad de letras en ella
# # La función contar_letras toma una palabra como argumento y devuelve la cantidad de letras en ella
# # La función main se encarga de solicitar la entrada del usuario y mostrar el resultado.
# # Definición de la función contar_letras
# # def contar_letras(palabra):        
