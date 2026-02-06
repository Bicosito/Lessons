# Task 14 
txt = []
us, vr = 0, 0
while True:    
    n = int(input('Введите число от 1 до 100000 '))
    if n > 100000 or n < 1:
        print('Введено число, превышающее условия задания.')
    else:
        break   

while us == 0:
    k = 0
    txt = list(map(int, input(f'Введите {n} числа(ел) через пробел от 1 до 10000000000 ').split()))
    if len(txt) != n:
        print('Вы ввели количество чисел отличное, от требуемого.')
        continue
    for i in range(len(txt)):
        if txt[i] > 10000000000 or txt[i] < 1:
            print('Введено число, превышающее условия задания.')
        else:
            k += 1
    if k == len(txt):
        us = 5
txt.insert(0, txt[-1])
txt.pop()    
print(*txt)