def INDEX(val):
    List = [5,7,9,-7,10,20,1,15]
    ind = List.index(val,0,)
    print(f'The index of {val} is {ind}.')

value = int(input('Do you want to know the index of which value? > '))
INDEX(value)