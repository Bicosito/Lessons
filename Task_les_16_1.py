class Kassa(object):
    money = 0
    
    def __init__(self, m):
        self.money = m

    def top_up(self, x):
        self.money += x
    
    def count_1000(self):
        print(self.money // 1000)
    
    def take_away(self, m):
        if self.money - m >= 0:
            self.money -= m
        else:
            print("В кассе недостаточно средтв! ")

kas = Kassa(0)
while True:
    x = int(input('Выберите действие:\n' \
    '1 - пополнить кассу\n' \
    '2 - вывести количество тысяч в кассе\n' \
    '3 - забрать из кассы\n'))
    if x == 1:
        m = int(input('Введите сумму '))
        kas.top_up(m)
        print(f'Касса  пополнена на {m} рублей, сумма в кассе {kas.money}')
    elif x == 2:
        kas.count_1000()
    elif x == 3:
        m = int(input('Введите сумму, которую планируете забрать '))
        kas.take_away(m)
        print(f'Cумма в кассе {kas.money}')