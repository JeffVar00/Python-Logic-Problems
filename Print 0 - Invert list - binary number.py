
def ImprimirCero(n):
    print(n)
    if n == 0:
        return 0
    else:
        ImprimirCero(n - 1)

def InvertirNum(n):
    print(n % 10)
    if n > 10:
        n = n/10
        InvertirNum(int(n))

def binario(a):
    if a > 1:
        binario(a / 2)
        a = int(a)
        print(a % 2)

def main():
    print("Binario {}".format(12))
    binario(12)
    print("valor invertido")
    InvertirNum(123)
    print("Valores hasta 0")
    ImprimirCero(5)


if __name__ == '__main__':
    main()