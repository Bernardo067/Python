a = float(input("insira sua altura"))
p = float(input("insira seu peso"))

if a < 1.20:
    if p < 60:
        print("class A")
    elif p >= 60 and p < 90:
        print("class D")
    else:
        print("class G")

elif a >= 1.20 and a < 1.70:
    if p < 60:
        print("class B")
    elif p >= 60 and p < 90:
        print("class E")
    else:
        print("class H")

else:
    if p < 60:
        print("class C")
    elif p >= 60 and p < 90:
        print("class F")
    else:
        print("class I")