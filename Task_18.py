#Task 18
txt = list(map(int, input(f'Введите последовательность чисел через пробел от 1 до 10000000000 ').split()))
res = ['NO']
for i in range(1, len(txt)):
    for j in range(i):
        if txt[j] == txt[i]:
            res.append('YES')
            break
    if len(res) == i:
        res.append('NO')   
print(*res)