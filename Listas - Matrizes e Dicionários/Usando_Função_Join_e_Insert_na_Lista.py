def EscreveTexto ():
    textoCompleto = list()
    counter = 0
    validacao = ''
    while True:
        texto = str(input())
        textoCompleto.insert(counter, texto)
        valicadao = str(input('Deseja escrever outro parágrafo? [S/N] ')).upper()
        counter += 1
        if valicadao != 'S':
            break
        
    print(''.join(texto[:]), end=' ')

EscreveTexto()