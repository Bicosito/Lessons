# Task 8
n = int(input('Введите количество чисел '))
ch = 0
for i in range(n):
    h = int(input('Введите число '))
    if h == 0:
        ch += 1
print(f'Введено чисел, равных нулю - {ch}')