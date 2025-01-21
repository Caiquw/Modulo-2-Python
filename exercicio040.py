nota1 = float(input("Nota parcial:\n"))
nota2 = float(input("Nota final:\n"))

media = (nota1 + nota2)/2

if media < 5:
    print("Reprovado!!!")
elif media < 6.9:
    print("Recuperação!!!")
elif media >= 7:
    print("Aprovado!!!")