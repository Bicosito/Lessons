# Task 7
mnv, vlm, vli = int(input('Введите минимальную сумму инвестиций ')), int(input('Введите сумму накоплений Майкла ')), int(input('Введите сумму накоплений Ивана '))
if vlm >= mnv and vli >= mnv:
    print('2')
elif vlm >= mnv or vli >= mnv:
    if vlm >= mnv:
        print('Mike')
    else:
        print('Ivan')
elif vlm + vli >= mnv:
    print('1')
else:
    print('0')