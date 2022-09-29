import random


numeros = [0] * 10000
contador = [0] * 10

for i in range(len(numeros)):
    numeros[i] = random.randint(1,10)
    print(numeros[i], end=' ')


for i in range(len(numeros)):
    num = numeros[i]                
    contador[num - 1] += 1
    
# elementos 0  0  1  0  0  2  0  0  2  0 
#   indices 0  1  2  3  4  5  6  7  8  9
#           1s 2s 3s 4s 5s 6s 7s 8s 9s 10s

for i in range(len(contador)):
    print(f'\nO número {i+1} aparece {contador[i]} vezes')