import random
cont = 0
cont_par = 0
cont_inpar = 0

while cont <= 200:
    num = (random.randint(1, 1000))
    print(num)
    cont += 1
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_inpar += 1
print(f"tem {cont_par} numeros pares, e {cont_inpar} numeros impares")
