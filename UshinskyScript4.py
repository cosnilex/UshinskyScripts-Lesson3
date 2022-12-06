#!/usr/bin/python3
"""** C обработкой отрицательного дискриминанта (с комплексными числами), со случаем, если коэффициенты являются комплексными числами."""

print(f'a*x**2+b*x+c=0')

a = complex(input(f'Введите значение a: '))
b = complex(input(f'Введите значение b: '))
c = complex(input(f'Введите значение c: '))

discriminant = b**2 - 4*a*c
print(f'Дискриминант = {discriminant}')
if discriminant == 0:
    x = -b / (2 * a)
    print(f'x =  {x}')
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
