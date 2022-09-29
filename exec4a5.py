x = int(input("insira o primeiro numero do triangulo...."))
y = int(input("insira o segundp numero do triangulo....."))
z = int(input("insira o terceiro numero do triangulo...."))

if x >= y + z or y >= x + z >= x + y :
    print("triangulo impossível")
else:
    if x == y == z:
        print("equilátero")
    elif x != y != z:
        print("escaleno")
    else:
        print('isóceles')