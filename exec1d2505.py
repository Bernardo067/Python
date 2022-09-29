def verificar(num):
    if num > 0:
        return True
    elif num < 0:
        return False
    else:
        return 'Neutro'


# ler um numero do teclado
# chamar a função
num = int(input('Digite um número: '))
result = verificar(num)
print(result)