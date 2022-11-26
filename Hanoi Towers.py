import os

class pila:
    def __init__(self):  # inicializacion de la pila
        self.items = []  # items es una lista

    def isEmpty(self):
        return self.items == []

    def incluirDisco(self, item):
        self.items.append(item)  # append, metodo agregar de la pila

    def extraerDisco(self):
        return self.items.pop()  # pop, metodo extraer de la pila

    def mostrarDiscos(self):
        i = 1
        while i <= len(self.items):
            print(("_" * self.items[len(self.items) - i] * 2).center(20, " "))
            i += 1

    def inspeccionarDisco(self):
        return self.items[len(self.items) - 1]

    def tamano(self):
        return len(self.items)


def hanoiRecursivo(n, A=1, B=2, C=3):  # solo muestra movimientos, no es con pilas
    if n == 1:
        print(A, "a", C)
    else:
        hanoiRecursivo(n - 1, A, C, B)
        print(A, "a", C)
        hanoiRecursivo(n - 1, B, A, C)


def mostrarTorres(t1, t2, t3):
    print("\nTORRE 1")
    t1.mostrarDiscos()
    print("TORRE 2")
    t2.mostrarDiscos()
    print("TORRE 3")
    t3.mostrarDiscos()


def validarGanador(torre, torres):  # no funciona
    if torre.tamano() == torres:
        return True
    else:
        return False


def jugarHanoi(torres):
    ganador = False
    vidas = 3
    movimientos = 0
    t1 = pila()
    t2 = pila()
    t3 = pila()

    while torres > 0:
        t1.incluirDisco(torres)
        torres -= 1

    while vidas > 0 and ganador == False:

        os.system("cls")
        mostrarTorres(t1, t2, t3)

        print("\n----Digite su jugada----")
        opc1 = int(input("(Torre 1 2 o 3) De: "))
        opc2 = int(input("(Torre 1 2 o 3) Hacia: "))

        if opc1 == opc2:
            print("No se puede mover a su misma torre")
            os.system("pause")
        elif opc1 == 1 and opc2 == 2:
            if t1.isEmpty():
                print("Torre vacia")
                os.system("pause")
            elif t2.isEmpty():
                t2.incluirDisco(t1.extraerDisco())
                movimientos += 1
                print("Movimiento: De 1 a 2")
                print("Movimientos: {}".format(movimientos))
                os.system("pause")
            else:
                if t2.inspeccionarDisco() < t1.inspeccionarDisco():
                    print("Lo sentimos perdiste una vida, intentalo de nuevo")
                    vidas -= 1
                    print("Vidas restantes: {}".format(vidas))
                    if vidas == 0:
                        print("Lo sentimos perdiste")
                    os.system("pause")
                else:
                    t2.incluirDisco(t1.extraerDisco())
                    movimientos += 1
                    print("Movimiento: De 1 a 2")
                    print("Movimientos: {}".format(movimientos))
                    os.system("pause")

        elif opc1 == 2 and opc2 == 1:
            if t2.isEmpty():
                print("Torre vacia")
                os.system("pause")
            elif t1.isEmpty():
                t1.incluirDisco(t2.extraerDisco())
                movimientos += 1
                print("Movimiento: De 1 a 2")
                print("Movimientos: {}".format(movimientos))
                os.system("pause")
            else:
                if t1.inspeccionarDisco() < t2.inspeccionarDisco():
                    print("Lo sentimos perdiste una vida, intentalo de nuevo")
                    vidas -= 1
                    print("Vidas restantes: {}".format(vidas))
                    if vidas == 0:
                        print("Lo sentimos perdiste")
                    os.system("pause")
                else:
                    t1.incluirDisco(t2.extraerDisco())
                    movimientos += 1
                    print("Movimiento: De 2 a 1")
                    print("Movimientos: {}".format(movimientos))
                    os.system("pause")

        elif opc1 == 1 and opc2 == 3:
            if t1.isEmpty():
                print("Torre vacia")
                os.system("pause")
            elif t3.isEmpty():
                t3.incluirDisco(t1.extraerDisco())
                movimientos += 1
                print("Movimiento: De 1 a 2")
                print("Movimientos: {}".format(movimientos))
                os.system("pause")
            else:
                if t3.inspeccionarDisco() < t1.inspeccionarDisco():
                    print("Lo sentimos perdiste una vida, intentalo de nuevo")
                    vidas -= 1
                    print("Vidas restantes: {}".format(vidas))
                    if vidas == 0:
                        print("Lo sentimos perdiste")
                    os.system("pause")
                else:
                    t3.incluirDisco(t1.extraerDisco())
                    movimientos += 1
                    print("Movimiento: De 1 a 3")
                    print("Movimientos: {}".format(movimientos))
                    if validarGanador(t3, torres):
                        ganador = True
                        print("Ganaste!")
                    os.system("pause")

        elif opc1 == 3 and opc2 == 1:
            if t3.isEmpty():
                print("Torre vacia")
                os.system("pause")
            elif t1.isEmpty():
                t1.incluirDisco(t3.extraerDisco())
                movimientos += 1
                print("Movimiento: De 1 a 2")
                print("Movimientos: {}".format(movimientos))
                os.system("pause")
            else:
                if t1.inspeccionarDisco() < t3.inspeccionarDisco():
                    print("Lo sentimos perdiste una vida, intentalo de nuevo")
                    vidas -= 1
                    print("Vidas restantes: {}".format(vidas))
                    if vidas == 0:
                        print("Lo sentimos perdiste")
                    os.system("pause")
                else:
                    t1.incluirDisco(t3.extraerDisco())
                    movimientos += 1
                    print("Movimiento: De 3 a 1")
                    print("Movimientos: {}".format(movimientos))
                    os.system("pause")

        elif opc1 == 3 and opc2 == 2:
            if t3.isEmpty():
                print("Torre vacia")
                os.system("pause")
            elif t2.isEmpty():
                t2.incluirDisco(t3.extraerDisco())
                movimientos += 1
                print("Movimiento: De 1 a 2")
                print("Movimientos: {}".format(movimientos))
                os.system("pause")
            else:
                if t2.inspeccionarDisco() < t3.inspeccionarDisco():
                    print("Lo sentimos perdiste una vida, intentalo de nuevo")
                    vidas -= 1
                    print("Vidas restantes: {}".format(vidas))
                    if vidas == 0:
                        print("Lo sentimos perdiste")
                    os.system("pause")
                else:
                    t2.incluirDisco(t3.extraerDisco())
                    movimientos += 1
                    print("Movimiento: De 3 a 2")
                    print("Movimientos: {}".format(movimientos))
                    os.system("pause")

        elif opc1 == 2 and opc2 == 3:
            if t2.isEmpty():
                print("Torre vacia")
                os.system("pause")
            elif t3.isEmpty():
                t3.incluirDisco(t2.extraerDisco())
                movimientos += 1
                print("Movimiento: De 1 a 2")
                print("Movimientos: {}".format(movimientos))
                os.system("pause")
            else:
                if t3.inspeccionarDisco() < t2.inspeccionarDisco():
                    print("Lo sentimos perdiste una vida, intentalo de nuevo")
                    vidas -= 1
                    print("Vidas restantes: {}".format(vidas))
                    if vidas == 0:
                        print("Lo sentimos perdiste")
                    os.system("pause")
                else:
                    t3.incluirDisco(t2.extraerDisco())
                    movimientos += 1
                    print("Movimiento: De 2 a 3")
                    print("Movimientos: {}".format(movimientos))
                    if validarGanador(t3, torres):
                        ganador = True
                        print("Ganaste!")
                    os.system("pause")
        else:
            print("Digite una opcion valida")


def main():

    n = 0
    while n != 2:
        os.system("cls")
        # Hanoi manual
        n = int(input("1-Juego Hanoi\n2-Salir\n"))
        if n == 1:
            torres = int(input("Digite la cantidad de torres a jugar: "))
            jugarHanoi(torres)
            os.system("pause")
        else:
            break

    # Sebastián Long Segura Méndez
    # Jacksem Cortes Vasquez
    # Jeff Vargas Barrantes
    # Geysel Garcia Fuentes


if __name__ == '__main__':
    main()

# como usar una pila obtenido de
# https://runestone.academy/runestone/static/pythoned/BasicDS/ImplementacionDeUnaPilaEnPython.html
