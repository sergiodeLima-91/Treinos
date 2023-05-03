from time import sleep

def Counter(s,fl,ct):
    if ct == 1:
        print(f'Contagem Progressiva de {s} até {fl}:')
        while True:
            print(f'{s} ', end='')
            s += 1
            if s > fl:
                break
    elif ct == 2:
        print(f'Contagem Regressiva de {s} até {fl}:')
        while True:
            
            print(f'{s} ', end='')
            s -= 1
            if  s < fl:
                break
    


countageType = int(input('Qual é o tipo de contagem? [1 - Progressiva 2 - Regressiva]' ))
start = int(input('Qual é o número INICIAL da contagem? '))
finishLine = int(input('Qual é o número FINAL da contagem? '))


Counter(start, finishLine,countageType)