nota1 = float(input("nota 1     "))
nota2 = float(input("nota 2     "))
nota3 = float(input("nota 3     "))

media = (nota1 + nota2 + nota3) / 3 

if media >= 6 :
    print("APROVADO")
elif media >= 3 :
    print(f"EXAME , a nota necessária para passar é : {12 - media}")
else:
    print("REPROVADO")