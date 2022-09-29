media_classe = 0
reprovado = 0
exame = 0
aprovado = 0

for cont in range(1, 7):
    print(f'\n==== DADOS DO {cont}o ALUNO ====')
    nota1 = float(input('Digite a 1a nota: '))
    nota2 = float(input('Digite a 2a nota: '))
    media = (nota1 + nota2) / 2
    print(f'Sua média é {media:.1f}')

    media_classe += media

    if media <= 3:
        print(f'REPROVADO :-(')
        reprovado += 1
    elif media < 7:
        print(f'EXAME :-|')
        exame += 1
    else:
        print(f'APROVADO :-)')
        aprovado += 1

print(f'A média da classe é {(media_classe/cont):.1f}')
print(f'Total de aprovados: {aprovado}')
print(f'Total de reprovados: {reprovado}')
print(f'Total de exame: {exame}')