'''
 Реализовать два небольших скрипта:
 а) бесконечный итератор, генерирующий целые числа,
 начиная с указанного,
 б) бесконечный итератор, повторяющий элементы
 некоторого списка, определенного заранее.
 Подсказка: использовать функцию count() и cycle()
 модуля itertools.
 '''

from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el)

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)
