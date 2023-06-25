def par():
    a = str(input('Введите строку: '))
    b = a[::-1]
    if a == b:
        print('True')
    else:
        print('False')
par()