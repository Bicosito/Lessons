# Task 17
def uslovie(mn, mx):
    while True:    
        vx = int(input(f'Введите число от {mn} до {mx} '))
        if vx > mx or vx < mn:
            print('Введено число, превышающее условия задания.')
        else:
            break   
    return vx
s1 = uslovie(1, 100000)
s2 = uslovie(1, 100000)
sp1 = []
sp2 = []
for i in range(s1):
    k = int(input(f'Введите {i+1} число 1 списка '))
    sp1.append(k)
for i in range(s2):
    k = int(input(f'Введите {i+1} число 2 списка '))
    sp2.append(k)
us1 = set(sp1)
us2 = set(sp2)
print(len(us1.intersection(us2)))