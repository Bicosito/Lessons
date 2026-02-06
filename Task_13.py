# Task 13
txt = []
i = 0
n = int(input('Введите число '))
while i < n:
    k = input('Введите число строки от 1 до 10000 ')
    if int(k) >= 1 and int(k) <= 10000:
        txt.append(k)
        i += 1
    else:
        print('Введено число, превышающее условия задания.')
print(*list(reversed(txt)))