# Task 15 poka hz
txt = []

def uslovie(mn, mx, st):
    while True:    
        vx = int(input(f'Введите {st} от {mn} до {mx} '))
        if vx > mx or vx < mn:
            print('Введено число, превышающее условия задания.')
        else:
            break   
    return vx
m = uslovie(1, 10000000, 'максимальную массу лодки')
n = uslovie(1, 100, 'количество рыбаков')
for i in range(n):
    k = int(input(f'Введите вес  {i+1} рыбака '))
    if 1 <= k <= m:
        txt.append(k)
    else:
        i -= 1
txt.sort()
left = 1
boats = 0
while left <= n - 1:
    if txt[left-1] + txt[left] > m:
        boats += 1
        left += 1
    else:
        boats += 1
        left += 2
print(boats)


