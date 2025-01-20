#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

salario = float(input("Informe seu salário:\n"))
valorcasa = float(input("Informe o valor da casa:\n"))
anos = float(input("Informe em quantos anos ele ira pagar:\n"))


prestacao = valorcasa / (12 * anos)


print("Prestação a pagar: ",prestacao)

if prestacao > ((salario * 30)/ 100):
    print("O empréstimo foi negado!!!")

elif prestacao < ((salario * 30)/ 100):
    print("O empréstimo foi aceito!!!")

