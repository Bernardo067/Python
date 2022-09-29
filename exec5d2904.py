num = int(input("insira um numero..."))
if num % 10 == 0:
    print("o numero é divizível por 10, por 5 e por 2")
elif num % 5 == 0:
    print("o numero é divizível por 5")
elif num % 2 == 0 :
    print("o numero é divizível por 2")
else:
    print("o numero não é divizível por 10/5/2")