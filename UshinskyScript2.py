#!/usr/bin/python3
"""Предыдущее, но скрипт бесконечный (каждый раз спрашивается куда движение и выводится результат). Обязательно стоп-слово."""

x = 0
y = 0
stop_word='cont'
while stop_word=='cont':
    print(f'*up, down, left, right*')
    side=str(input(f'Введите сторону: '))
    print(f'*Любое натуральное, целое число*')
    step=int(input(f'Введите шаг: '))
    if side == "right" and step >0:
        y+=0
        x+=step
        print(f'Вы в точке ({x},{y})')
    elif side == "left" and step >0:
        y+=0
        x-=step
        print(f'Вы в точке ({x},{y})')
    elif side == "up" and step>0:
        y+=step
        x+=0
        print(f'Вы в точке ({x},{y})')
    elif side == "down" and step >0:
        y-=step
        x+=0
        print(f'Вы в точке ({x},{y})')
    else:
        print(f'Проверьте правильность введенных данных')
    stop_word=str(input(f'Хотите продолжить? (Для продолжения введите \"cont\" для остановки \"stop\")\n'))
    if stop_word=='stop':
        print(f'Последня точка: ({x},{y})\nДо новых встреч!')
        break
        
    elif stop_word=='cont':
        continue
    else:
        print(f'Неверно введено стоп-слово, попробуйте \"stop\" или \"cont\" ')
        stop_word=str(input(f'Хотите продолжить? (Для продолжения введите \"cont\" для остановки \"stop\")\n'))
