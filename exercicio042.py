seg1 = float(input("Primeiro segmento:\n"))
seg2 = float(input("Segundo segmento:\n"))
seg3 = float(input("Terceiro segmento:\n"))

if (seg1 + seg2) > seg3 and (seg3 + seg1) > seg2 and (seg3 + seg2) > seg1:
        print("Pode ser um triângulo!!") 
        if seg1 == seg2 != seg3 or seg1 == seg3 != seg2 or  seg2 == seg3 != seg1:
            print("É um triângulo isósceles")
        elif seg1 == seg2 == seg3:
            print("É um triângulo equilátero")
        elif seg1 != seg2 != seg3:
            print("É um triângulo escaleno")        

else:
    print("Não pode ser um triângulo!!")

