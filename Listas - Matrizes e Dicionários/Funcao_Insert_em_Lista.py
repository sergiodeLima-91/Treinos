a = []
c = 0
while True:
    frase = str(input())
    a.insert(c, frase)
    c += 1
    if frase == 'exit':
        a.pop()
        break
print(''.join(map(str, a[:])), end='')