"""Mayor de tres números"""
# Pide tres números y muestra el mayor

print("====MAyor de tres números====")
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))
if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3
print(f"El mayor de {numero1}, {numero2} y {numero3} es: {mayor}")

print("====Fin del programa====")
