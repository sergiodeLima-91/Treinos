def COUNT(co):
    List = [5,7,9,-7,7,10,20,1,15,5,9,20,22,50,50,5,10,20]
    numberOfTimes = List.count(co)
    if numberOfTimes == 0:
        print(f'ValueError: The number {co} is not present in the list!')
    else:
        print(f'The number {co} appears {numberOfTimes} times in the list.')


number = int(input('Insert the number > '))
COUNT(number)
