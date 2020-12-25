"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения
для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми
другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального
значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

#  Поиск минимального значения

from random import randint
# Квадратичная сложность
def min_value(first):
    for i in first:
        minimal = True
        for j in first:
            if i > j:
                minimal = False
        if minimal:
            return i

# Линейная сложность 
def min_value (first):
    minimal = first[0]
    for i in first:
        if i < minimal:
            minimal = i
    return minimal

