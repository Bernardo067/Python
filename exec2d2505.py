def converter(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    seg = resto % 60

    print(f'{horas:02d}:{minutos:02d}:{seg:02d}')


segundos = int(input('Digite os segundos para conversão: '))
converter(segundos)