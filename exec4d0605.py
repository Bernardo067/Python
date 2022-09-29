menor = 9999999
cont = 0
while cont < 10:
    num = int(input())
    if num < menor:
        menor = num
        cont += 1
    else:
        cont += 1
print(f"o menor numero é {menor}")