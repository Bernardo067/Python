def calcular_imc(peso, alt):
    return  peso / (alt * alt)

def classificar(imc):
    if imc < 18.5:
        return 'subpeso'
    elif imc < 25:
        return 'normal'
    elif imc < 29.6:
        return 'sobrepeso'
    elif imc < 35:
        return 'obsidade grau 1'
    elif imc < 40:
        return 'obsidade grau 2'
    else:
        return 'obsidade grau 3'


# ===== programa
peso = float(input('Digite o peso: '))
alt = float(input('Digite a altura: '))
imc = calcular_imc(peso, alt) # chamando a função

print(classificar(imc)) # chamando a função