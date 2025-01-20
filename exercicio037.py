
escolha = int(input("""ESCOLHA UM A SEGUIR:\n
                    [1] Binário
                    [2] Hexadecimal
                    [3] Octal
                    """))
texto = ""
numero = int(input("Digite um numero inteiro qualquer\n"))
if escolha == 1:
    print(bin(numero)[2:])

elif escolha == 2:
    print(hex(numero)[2:])
    
elif escolha == 3:
    print(oct(numero)[2:])