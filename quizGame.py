from rich.console import Console
from rich.table import Table
console = Console()

pts = 0
print('Добро пожаловать!')
name = input('Введите Ваше имя: ')
start = input('Начинаем игру? ')

if start.lower() == 'да' or start == 'yes':
    print('Тогда приступим :) ')
else:
    quit()

question = input('Столица Испании? ')
if question.lower() == 'мадрид' or question.lower() == 'madrid':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица Украины? ')
if question.lower() == 'киев' or question.lower() == 'kiev':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица Германии? ')
if question.lower() == 'берлин' or question.lower() == 'berlin':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица Италии? ')
if question.lower() == 'рим' or question.lower() == 'rome':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица США? ')
if question.lower() == 'вашингтон' or question.lower() == 'washington':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица Португалии? ')
if question.lower() == 'лиссабон' or question.lower() == 'lisbon':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица Англии? ')
if question.lower() == 'лондон' or question.lower() == 'london':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица Швейцарии? ')
if question.lower() == 'берн' or question.lower() == 'berne':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

question = input('Столица Франции? ')
if question.lower() == 'париж' or question.lower() == 'paris':
    pts += 1
    print('Верно! Вы получаете 1 бал!')
else:
    pts -= 1
    print('К сожалению это неверный ответ :(')

print('Вот и подошла игра к завершению!')
print()
table = Table(show_header=True, header_style='bold magenta')
table.add_column('Имя', style='dim', width=12, justify='center')
table.add_column('Набрано Очков', justify='center')
table.add_row(name, str(pts))
console.print(table)
print()
print('Это:', str((pts / 9) * 100), '%', 'из 100%')
if pts >= 8:
    print('Вы настоящий знаток!')
elif pts >= 5 < 8:
    print('Хорошие знания!')
else:
    print('Вам стоит подтянуть Ваши знания!')
