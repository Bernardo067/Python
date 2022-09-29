num = int(input("insira um numero..."))
if num % 2 == 0 :
    if num > 0:
        print("o numero é positivo e par")
    else:
         print("o numero é negativo e par")
elif num > 0:
    print("o numero é positivo e ímpar")
else:
    print("o numero é negativo e ímpar")