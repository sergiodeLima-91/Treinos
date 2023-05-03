from random import choice

Error = False
NumberQuantity = 0
FantasyName = 'S U P E R   J O G O   D E   A Z A R   2 0 0 0: S E U   J O G O ,   N Ó S S O    L U C R O !'

print('=' * len(FantasyName))
print(FantasyName)
print('=' * len(FantasyName))

while Error == False:
    def loteria(game, quantity):
        Numbers = []
        PlayerNumbers = []
        if game == 1:
            for counter1 in range(60):
                Numbers.append(counter1)
            for counter1 in range(quantity):
                PlayerNumbers.append(choice(Numbers))
            print('Os números sorteados na Mega Sena foram: ' ,' '.join(map(str, PlayerNumbers)))
        elif game == 2:
            for counter2 in range(100):
                Numbers.append(counter2)
            for counter2 in range(50):
                PlayerNumbers.append(choice(Numbers))
            print('Os números sorteados na Loto Mania foram: ' ,' '.join(map(str, PlayerNumbers)))
        elif game == 3:
            for counter3 in range(25):
                Numbers.append(counter3)
            for counter3 in range(quantity):
                PlayerNumbers.append(choice(Numbers))
            print('Os números sorteados na Loto Fácil foram: ' ,' '.join(map(str, PlayerNumbers)))

    Menu = 'Escolha um dos jogos abaixo: '
    print('=' * len(Menu))
    print(Menu)
    print('=' * len(Menu))
    print('(1) - Mega Sena')
    print('(2) - Loto Mania')
    print('(3) - Loto Fácil')
    print('(4) - Sair')
    SelectedGame = int((input('Digite o número correspondente > ')))
    
    while True:
        if SelectedGame < 1 or SelectedGame > 4:
            print(f'O número {SelectedGame} não corresponde a nenhuma das opções! Tente novamente!')
            break
        if SelectedGame == 4:
            print('Boa sorte!')
            Error = True
            break
        elif SelectedGame == 1:
            NumberQuantity = int((input('Quantos números deseja jogar? [Minimo: 6 / Máximo: 15]> ')))
            if NumberQuantity < 6 or NumberQuantity > 15:
                print('Digite um número entre 6 e 15!')
                break
            loteria(SelectedGame, NumberQuantity)
            break
        elif SelectedGame == 2:
            loteria(SelectedGame, NumberQuantity)
            break
        elif SelectedGame == 3:
            NumberQuantity = int(input('Quantos números deseja jogar? [Minimo: 15 / Máximo: 20]> '))
            if NumberQuantity < 15 or NumberQuantity > 20:
                print('Digite um número entre 15 e 20!')
                break
            loteria(SelectedGame, NumberQuantity)
            break