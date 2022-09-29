lista = [0]*5
cont=0
for i in range(len(lista)):
    lista[i] = float(input())
for i in range(len(lista)):
    if lista[i] < 50 and lista[i] > 10:
            cont +=1
print(cont)