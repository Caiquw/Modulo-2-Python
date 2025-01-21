import math
peso = float(input("Insira seu peso:\n"))
altura = float(input("Insira sua altura:\n"))

imc = peso / pow(altura,2)

print(round(imc,2))

if imc < 18.5:
    print("Abaixo do Peso")
elif 18.5 <= imc <= 25:
    print("Peso ideal")
elif 25.1 <= imc <= 30:
    print("Sobrepeso")
elif 30 <= imc <= 40:
    print("Obesidade")
elif imc > 40:
    print("Obesidade mórbida")