par = []
impar = []
lst = []
def separar(lista , lstpar , lstimpar):
    for i in range(len(lista)):
        if lista[i] % 2 ==0:
            lstpar.append(lista[i])
        else:
            lstimpar.append(lista[i])
while(True):
    num = int(input("digite o numero"))
    lst.append(num)
    escolha = (input("deseja continuar?"))
    if escolha == "não" or escolha == "nao" or escolha == "n":
        break 
separar(lst , par , impar)

print(par)
print(impar)