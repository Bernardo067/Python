def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def validar_nota(nota):
    while not (nota >= 0 and nota <= 10):
        print('==>Erro: nota inválida.')
        nota = float(input('\nDigite novamente: '))

    return nota


# ========== o programa ==================
nota1 = float(input('Digite a 1a nota: '))
nota1 = validar_nota(nota1)

nota2 = float(input('Digite a 2a nota: '))
nota2 = validar_nota(nota2)
nota3 = float(input('Digite a 3a not
a: '))
nota3 = validar_nota(nota3)

media = calcular_media(nota1, nota2, nota3)
print(f'A média é {media:.1f}')