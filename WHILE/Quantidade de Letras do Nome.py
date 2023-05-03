def CharNameQuantity():
    Counter = 0
    QuestionRegister = []
    Words = []

    while True:
        Counter += 1
        name = str(input(f'Digite um nome ou frase com {Counter} letra (s): '))
        Words.append(name)

        if len(name) != Counter:
            print(f'{name} não possui {Counter} letra (s)! Tente novamente!')
            break

        Question = str(input('Deseja continuar [S/N]? ')).upper()
        QuestionRegister.append(Question)
        if Question == 'N':
            print(f'Palavras digitas por quantidade de caracteres: {Words}')
            break

CharNameQuantity()
