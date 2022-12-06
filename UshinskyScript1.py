#!/usr/bin/python3
"""Написать скрипт для движения персонажа влево, вправо, вверх и вниз по координатам x и y по координатной оси, начальная позиция персонажа (0;0)"""

x = 0
y = 0
moves = ["up", "down", "left", "right"]
print(f'*up, down, left, right*')
move =str(input(f'В какую сторону вы хотите двигаться? '))

if move not in moves:
    print('wrong move')
    exit(1)
    

step =int(input(f'На сколько шагов вы хотите сдвинуться в данном направлении? '))

if move == 'left':
    y = 0
    if step > 0:
        x = -step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})')
elif move == 'right':
    y = 0
    if step > 0:
        x = step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})') 
elif move == 'up':
    x = 0
    if step > 0:
        y = step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})')
elif move == 'down':
    x = 0
    if step > 0:
        y = -step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})')
else:
    print(f'Несуществующий вектор движения, выберите из: up, down, left, right')
