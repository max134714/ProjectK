x = float(input('x=  '))

if 0 < x < 7:
    print(' x входит в заданный диапазон')
    y = 2 * x - 5
    if y < 0:
        print(' y отрицательный')
    else:
        if y > 0:
            print(' y положительный')
        else:
            print('y = 0')
else:
    print('Введите что-нибудь другое')


if 0 < x < 7:
    print('x входит в заданный диапазон')
    y = 2 * x - 5
    if y < 0:
        print('y отрицательный')
    elif y > 0:
        print('y положительный')
    else:
        print('y = 0')

