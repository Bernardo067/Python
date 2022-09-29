def solving(numbers, k):
    for i in numbers:
        if (k - i) > 0:
            resto = k - i
            for i in numbers:
                if i == resto:
                    return True
        
l=[10, 15, 3, 7]
k=17
print(solving(l, k))