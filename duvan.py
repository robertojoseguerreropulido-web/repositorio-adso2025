# Calculadora sencilla

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

operacion = input("Elige la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir entre 0")
else:
    print("Operación no válida")
