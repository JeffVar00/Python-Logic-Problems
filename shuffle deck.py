def revolver(cartas):
    cartasAux = []
    nCartas = int(len(cartas)/2) 
    for i in range(nCartas):
        cartasAux.append(cartas[i+nCartas])
        cartasAux.append(cartas[i])
    return cartasAux

if __name__ == '__main__':
    cartasIniciales = []        
    aux = 0    
    [cartasIniciales.append(i+1) for i in range(int(input()))]    
    while True:
        aux+=1
        cartasIniciales = revolver(cartasIniciales)
        if cartasIniciales[0] == 1:
            break        
    print(aux)