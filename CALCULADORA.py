num1 = float(input("Ingrese el primer valor: "))
op = input("Ingrese la operación que desee realizar (+, -, / o *): ")
num2 = float(input("Ingrese el segundo valor: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("El operador ingresado no es válido.")