# Task 10
f = 0
while f < 5:
    a, b = int(input('Введите целое число А ')), int(input('Введите целое число В '))
    if a <= b:
        f = 10
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')
