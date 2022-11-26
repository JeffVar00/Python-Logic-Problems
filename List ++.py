
vec = [1, 2, 3, 4, 5]

def sumVec(vec):
    return sum(vec) #funcion ya presestablecida

def sumVecRecursiva(vec):
    if len(vec) == 1:
        return vec[0]
    else:
        return vec[0] + sumVecRecursiva(vec[1:]) # 1: descarta el primer elemento del vector, tipo 1 2 3, se elimina 1 y queda 2 3


print(sumVecRecursiva(vec))