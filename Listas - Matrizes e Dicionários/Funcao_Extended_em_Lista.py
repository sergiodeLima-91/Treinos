def Extend():
    matrixMain = []
    extend = []
    previous = 0
    while previous < 10:
        number = int(input(f'Digite qual é o número depois do {previous}: > '))
        extend.append(number)
        previous = number

    matrixMain.extend(extend)
    print(' '.join(map(str, matrixMain)))

Extend()