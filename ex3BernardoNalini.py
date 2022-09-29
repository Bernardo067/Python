def tarefa():
    fazerSol = input("irá fazer sol?")
    eFeriado = input("será feriado?")
    if fazerSol == "sim" or fazerSol == "s":
        fazerSol = True
    else : 
        fazerSol = False
    if eFeriado == "sim" or eFeriado== "s":
        eFeriado = True
    else : 
        eFeriado = False
    if fazerSol == True:
        if eFeriado == True:
            resp=("vai pra praia")
        else:
            resp=("passear no taquaral")
    else:
        if eFeriado == True:
            resp=("ver um filme")
        else :
            resp=("ler um livro")
    return resp
resp=tarefa()
print(resp)