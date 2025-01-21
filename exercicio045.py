valor = float(input("Valor a ser pago:\n"))

escolha = int(input("""""Escolha a forma de pagamento:\n
                    [1]Dinheiro/Cheque
                    [2]À Vista no cartão
                    [3]2x sem juros
                    [4]3x ou mais no cartão"""))
if escolha == 1:
    valor-= (valor * 10) / 100
    print("Valor a ser pago:",valor)
elif escolha == 2:
    valor-= (valor * 5) / 100
    print("Valor a ser pago:",valor)
elif escolha == 3:
    print("Valor a ser pago:",valor)
elif escolha == 4:
    valor+= (valor * 20) / 100
    print("Valor a ser pago:",valor)