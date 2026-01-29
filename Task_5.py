# Task 5
zn = int(input('Введите целое число '))
if zn % 2 == 0 and zn < 0:
    print('отрицательное четное число')
elif zn % 2 == 0 and zn > 0:
    print('положительное четное число')
elif zn == 0:
    print('нулевое число')
else:
    print('число не является четным')