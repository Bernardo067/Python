sal = 1015
aumento = 0.015 
for cont in range(2017, 2022):
    aumento = aumento * 2
    sal = (aumento * sal) + sal

print(sal)