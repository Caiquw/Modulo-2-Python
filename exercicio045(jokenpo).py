import random

cpu = [1,2,3]

print("Bem-vindo ao jogo Pedra Papel ou Tesoura\n")
print("para PEDRA digite [1]\npara PAPEL digite [2]\npara TESOURA digite [3]\n")

escolha = int(input("Escolha:\n"))
escolhacpu = random.choice(cpu)

if escolha == 1 and escolhacpu == 1:
    
    print("Você escolheu PEDRA\n")
    print("A CPU escolheu PEDRA\n")
    print("Empate")
elif escolha == 1 and escolhacpu == 2:
    print("Você escolheu PEDRA\n")
    print("A CPU escolheu PAPEL\n")
    print("Você perdeu")
elif escolha == 1 and escolhacpu == 3:
    print("Você escolheu PEDRA\n")
    print("A CPU escolheu TESOURA\n")
    print("Você ganhou")
elif escolha == 2 and escolhacpu == 1:
    print("Você escolheu PAPEL\n")
    print("A CPU escolheu PEDRA\n")
    print("Você ganhou")
elif escolha == 2 and escolhacpu == 2:
    print("Você escolheu PAPEL\n")
    print("A CPU escolheu PAPEL\n")
    print("Empate")
elif escolha == 2 and escolhacpu == 3:
    print("Você escolheu PAPEL\n")
    print("A CPU escolheu TESOURA\n")
    print("Você perdeu")
elif escolha == 3 and escolhacpu == 1:
    print("Você escolheu TESOURA\n")
    print("A CPU escolheu PEDRA\n")
    print("Você perdeu")
elif escolha == 3 and escolhacpu == 2:
    print("Você escolheu TESOURA\n")
    print("A CPU escolheu PAPEL\n")
    print("Empate")
elif escolha == 3 and escolhacpu == 3:
    print("Você escolheu TESOURA\n")
    print("A CPU escolheu TESOURA\n")
    print("Empate")