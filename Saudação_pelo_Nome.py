def Saudation(n):
    answer1 = f'Olá, {n}! Seja bem-vindo (a)!'
    answer2 = f'Espero que esteja tudo bem com você!'
    return answer1, answer2 

name = str(input('Qual é o seu nome? '))
print(Saudation(name))
