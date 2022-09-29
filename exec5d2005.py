lista_a = [0] * 4
lista_b = [0] * 7
lista_c = [0] * (len(lista_a) + len(lista_b))

print('----- INSIRA OS DADOS DA LISTA A -----')
for i in range(len(lista_a)):
    lista_a[i] = int(input())
    lista_c[i] = lista_a[i]

print('----- INSIRA OS DADOS DA LISTA B -----')
for i in range(len(lista_b)):
    lista_b[i] = int(input())
    lista_c[4 + i] = lista_b[i]

print('\n------ LISTA C ------')
for i in range(len(lista_c)):
    print(lista_c[i])