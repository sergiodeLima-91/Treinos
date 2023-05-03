def Remove(a, b, c):
    matriz = [1,2,3,4,5,6,7,8,9,10]
    matriz.remove(a)
    matriz.insert(c, b)
    print(' '.join(map(str, matriz)))


print('numbers = 1 2 3 4 5 6 7 8 9 10')
delete = int(input('Insert one number for is delete of the list > '))
add = int(input('Insert one number for is add in the list > '))
posicion = int(input('Insert position of the add > '))

Remove(delete, add, posicion)