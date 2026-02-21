# Task 19
petname = input('Введите имя питомца ')
vid = input('Введите вид питомца ')
petyear = int(input('Введите возраст питомца '))
pethz = input('Введите имя владельца ')
text = ''
if petyear % 10 == 1 and petyear != 11 and petyear % 100 != 11:
    text = 'год'
elif 1 < petyear % 10 <= 4 and petyear != 12 and petyear != 13 and petyear != 14:
    text = 'года'
else:
    text = 'лет'

pets = {

    petname:  {

        'Вид питомца': vid,# придумайте каким образом сюда внести информацию,

        'Возраст питомца': petyear,# придумайте каким образом сюда внести информацию,

        'Имя владельца': pethz# придумайте каким образом сюда внести информацию

}}
keys = pets.keys()
values = pets.values()
for key in pets.keys():
    print(f'Это {pets[petname]['Вид питомца']} по кличке {key}. Возраст: {pets[petname]['Возраст питомца']} {text}, Имя владельца: {pets[petname]['Имя владельца']}.')