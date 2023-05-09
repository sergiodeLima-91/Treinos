class ControleRemoto():
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    
    def mudarCanal(self, botao):
        if botao == '+':
            print('Aumentar Canal')
        elif botao == '-':
            print('Diminuir Canal')

controle_remoto1 = ControleRemoto('Azul','12cm', '3cm', '2cm')
print(controle_remoto1.cor)
Canal = str(input('Aumentar o diminuir canal? [+ / -] > '))
controle_remoto1.mudarCanal(Canal)

controle_remoto2 = ControleRemoto('Roxo','20cm', '5cm', '10cm')

