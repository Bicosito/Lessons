# Task 4
zn = int(input('Введите пятизначное число '))
des = zn % 100 // 10
ed = zn % 10
sot = zn % 1000 // 100
thos = zn % 10000 // 1000
thos2 = zn // 10000
print((des ** ed) * sot / (thos2 - thos))