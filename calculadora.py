from math import pow

escolha = str(input("""Escolha sua opção 
                    (+, -, *, /, **)\n"""))

n1 = 0.0
n2 = 0.0
resultado = 0.0


if escolha == "+":
   n1 = float(input("Insira o primeiro número:"))
   n2 = float(input("Insira o segundo número:",))
   resultado = n1 + n2
   print(f"{n1} + {n2} = {resultado}")

elif escolha == "-":
   n1 = float(input("Insira o primeiro número:"))
   n2 = float(input("Insira o segundo número:",))
   resultado = n1 - n2
   print(f"{n1} - {n2} = {resultado}")

elif escolha == "*":
   n1 = float(input("Insira o primeiro número:"))
   n2 = float(input("Insira o segundo número:",))
   resultado = n1 * n2
   print(f"{n1} * {n2} = {resultado}")

elif escolha == "/":
   n1 = float(input("Insira o primeiro número:"))
   n2 = float(input("Insira o segundo número:",))
   resultado = n1 / n2
   print(f"{n1} / {n2} = {resultado}")

elif escolha == "**":
   n1 = float(input("Insira o primeiro número:"))
   n2 = float(input("Insira o segundo número:",))
   resultado = float(pow(n1,n2) )
   
   print(f"{n1}^{n2} = {resultado}")
