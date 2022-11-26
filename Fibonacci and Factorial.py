def Factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * Factorial(numero - 1)

def Fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return Fibonacci(numero-2) + Fibonacci(numero-1)


def main():
    num = int(input("Factorial: "))
    num2 = int(input("Fibonacci: "))
    print("Factorial de {} = {}".format(num, Factorial(num)))
    print("Fibonacci de {} ".format(num2))
    i = 0
    while i < num2:
        if Fibonacci(i) >= 0:
            print(Fibonacci(i))
        i = i+1


if __name__ == '__main__':
    main()
