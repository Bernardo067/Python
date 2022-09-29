mes = int(input("insira o mês:     "))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == (10) or mes == (12):
    print("o mês tem 31 dias:    ")
elif mes == 2:
    ano = int(input("insira o ano:    "))
    if (ano % 4 == 0):
        print("o mês tem 29 dias")

    else :
        print("o mês tem 28 dias")
else:
    print("o mês tem 30 dias")