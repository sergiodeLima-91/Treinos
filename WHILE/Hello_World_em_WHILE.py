def HelloWorld():
    while True:
        print('Hello, world!')
        question = str(input('Deseja saudar o mundo mais uma vez? ')).upper()
        if question != 'S':
            return 'Thanks for playing whith us!'

HelloWorld()