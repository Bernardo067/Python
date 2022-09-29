import random
def ramdom(lst1 , lst2):
    for i in range(6):
        num = random.randint(1,6)
        lst1.append(num)
    for i in range(6):
        num = random.randint(1,6)
        lst2.append(num)
    lst = lst1 + lst2
    return lst
lst1 = []
lst2 = []
resul = ramdom(lst1 , lst2)
print(resul)
n = int(input("digite o numero que quer remover"))
resul.remove(n)
print(resul)