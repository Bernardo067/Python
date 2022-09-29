sexo = input('Digite o sexo (f/m): ')
altura = float(input("Digite a alutura: "))

if sexo.lower() == 'f':
    peso_ideal = (62.1 * altura)-44.7
    
else :
        peso_ideal = (72.7 * altura)-58

print(f"Seu peso ideal é {peso_ideal:.1f} KG")