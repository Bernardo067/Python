cont_idade=0
cont_eb=0
cont_altura=0

for cont in range(1,21):
    print(f"====={cont}º pessoa=====")
    cdo = input("cor dos olhos...").lower()
    while cdo != 'azuis' or cdo != 'azul' or cdo != 'verde' or cdo != 'verdes':
        print("ERROR")
        cdo = input("cor dos olhos...").lower()
    peso = float(input("peso..."))
    alt = float(input("altura"))
    idade = int(input("idade..."))
    if peso < 60 and idade > 50:
        cont_idade += 1
    if cdo == "azul" or cdo == "azuis":
        cont_eb += 1
    if alt > 1.68 and cdo != "verdes" and cdo != "verde":
        cont_altura += 1

print(f"tem {cont_idade} pessoas com mais de 50 anos e menos de 60 quilos")
print(f"já pessoas com olhos azuis compõe {cont_eb * 5}% das pessoas analisada")
print(f"e pessoas com mais de 1.68 e sem olhos verdes são {cont_altura}")