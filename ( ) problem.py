while True:
    try:
        entrada = input()
        lista = []
        abre = 0
        cierra = 0
        correct = True

        for i in entrada:
            if(i == "("):
                lista.append(i)
                abre += 1
            elif(i == ")"):
                lista.append(i)
                cierra += 1

        if(len(lista) % 2 != 0):
            correct = False
        else:
            if(lista[0] == ")"):
                correct = False
            elif(lista[len(lista) - 1] == "("):
                correct = False
            elif(abre != cierra):
                correct = False
        if correct:
            print("correct")
        else:
            print("incorrect")
    except(EOFError):
        break