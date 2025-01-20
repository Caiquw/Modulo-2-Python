import datetime 

anonasc = int(input("Digite seu ano de nascimento:\n"))

data = datetime.datetime.now()
ano = data.year

idade = data.year - anonasc


if (idade) < 18:
    print("Você ainda não tem obrigação de se alistar!!\n")
    
elif(idade) > 18:
    print("O prazo para alistamento já terminou")
else:
    print("Está na hora de se alistar")
    
