n1 = int(input("Insira um número:\n"))
n2 = int(input("Insira outro número\n"))

if n1 > n2:
    print(f"{n1} é maior que {n2}\n")
elif n2 > n1:
    print(f"{n1} é menor que {n2}\n")
elif n1 == n2:
    print(f"{n1} é igual a {n2}\n")
else:
    print("Algo deu errado")
