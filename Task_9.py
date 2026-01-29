# Task 9
n, d = 0, 1
while n <= 0: 
    n = int(input('Введите натуральное число '))
for i in range(1, n):
    if n % i == 0:
        d +=1

print(f'Натуральное число {n} имеет {d} натуральных делителей.')