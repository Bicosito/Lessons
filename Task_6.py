# Task 6
text = input('Введите слово ')
a, e, i, o, u, gl = 0, 0, 0, 0, 0, 0
zn = len(text)
for j in text:
    if j == 'a':
       a += 1 
    elif j == 'e':
        e += 1
    elif j == 'i':
        i += 1
    elif j == 'o':
        o += 1
    elif j == 'u':
        u += 1
gl = a + e + u + i + o
if a or e or u or i or o != 0:
    print(f'Данное слово состоит из {zn} букв, из них {gl} гласных и {zn - gl} согласных.')
    print(f'В слове содержится a - {a} шт., e - {e} шт., i - {i} шт., o - {o} шт., u - {u} шт.')
else:
    print('False')