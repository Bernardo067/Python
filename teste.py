def buscarMenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return i
nomes = [0]*5
quants = [0]*5
for i in range(len(quants)):
    nome = input()
    nomes[i] = nome
    quant = int(input())
    quants[i] = quant

menor = buscarMenor(quants)
print(menor)
