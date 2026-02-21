class Turtle(object):
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 0:
            self.s -=1
        else:
            print('S равен 1')
 
    def view(self):
        print(f'X: {self.x}| Y: {self.y}| S: {self.s}')


    def countmoves(self, x2, y2):
        x = self.x
        y = self.y
        s = self.s
        num = 0
        if x2 > y2:
            if y == y2:
                if abs(x2-x) == 1:
                    num += 1
                else:
                    num += abs(x2 - x) - s + 1
            else:
                if abs(y2 - y) == 1:
                    num += 1
                    if abs(x2-x) == 1:
                        num += 1
                    else:
                        num += abs(x2 - x) - s + 1
                else:
                    num += abs(y2 - y) - s + 1
                    if abs(x2-x) == 1:
                        num += 1
                    else:
                        num += abs(x2 - x) - abs(y2 - y) + 1
        else:
            if x == x2:
                if abs(y2-y) == 1:
                    num += 1
                else:
                    num += abs(y2 - y) - s + 1
            else:
                if abs(x2 - x) == 1:
                    num += 1
                    if abs(y2-y) == 1:
                        num += 1
                    else:
                        num += abs(y2 - y) - s + 1
                else:
                    num += abs(x2 - x) - s + 1
                    if abs(y2-y) == 1:
                        num += 1
                    else:
                        num += abs(y2 - y) - abs(x2 -x) + 1
        print(num)



tmp = Turtle(0, 0, 1)
while True:
    tmp.view()
    n = int(input('Выберите действие:\n' \
    '1 - Вверх\n' \
    '2 - Вниз\n' \
    '3 - Влево\n'
    '4 - Вправо\n'
    '5 - Увеличить скорость на 1\n'
    '6 - Уменьшить скорость на 1\n'
    '0 - Посчитать расстояние от текущего место положения до точки\n'))
    if n == 1:
        tmp.go_up()
    elif n == 2:
        tmp.go_down()
    elif n == 3:
        tmp.go_left()
    elif n == 4:
        tmp.go_right()
    elif n == 5:
        tmp.evolve()
    elif n == 6:
        tmp.degrade()
    elif n == 0:
        x2, y2 = int(input('Введите X2 ')), int(input('Введите Y2 '))
        tmp.countmoves(x2, y2)