def POP(elim):
    matrix = [5,7,9,-7,10,20,1,15]
    if elim == "all":
        matrix.clear()
        print('The matrix is clear.')
    else:
        matrix.pop(int(elim) - 1)
        print(' '.join(map(str, matrix)))


Eliminate = str(input('Insert the number corrsponding to the index or: > '))
POP(Eliminate)