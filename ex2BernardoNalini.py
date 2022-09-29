import math
def qdpt(num):
    m = math.sqrt(num)
    if m ** 2 == num :
        r = True
    else:
        r = False
    return r 
n = int(input("digite o numero "))
resp = qdpt(n)
if resp == True:
    print("é um quadrado perfeito")
else:
    print("não é um quadrado perfeito")