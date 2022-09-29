cont=0
cont_idade=0
cont_altura=0
acm_altura=0
cont_peso=0
for cont in range(26):
    cont+=1
    altura = float(input("digite a altura..."))
    idade = int(input("digite a idade..."))
    peso = float(input("digite o peso..."))

    if idade > 50:
        cont_idade += 1
    
    elif idade > 10 and idade < 20:
        cont_altura += 1
        acm_altura += altura
    
    elif peso < 40:
        cont_peso += 1

porc =(cont_peso*100)/25
media = acm_altura / cont_altura
print(f"tem {cont_idade} pessoas acima dos 50 anos.")
print(f"a média de altura das pessoas entre 10 e 20 anos é igual a {media}")