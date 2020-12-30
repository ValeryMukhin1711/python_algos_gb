"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Ряд строить программно - в самой же рекурсивной ф-ции
или даже обойтисть без создания ряда

Элемент в 2 раза меньше предыд и имеет противопол знак
"""


def rec_sum(n_count, start_num = 1, res_sum = 0):
    if n_count == 0:
        return res_sum
    else :
        res_sum = res_sum + start_num
        start_num = -start_num/2
        n_count -=1
    return rec_sum(n_count, start_num , res_sum  )    

str = input("Input number ")
try:
    numb = int(str)
except:
    print("Error! Input number")

print(rec_sum(numb, start_num = 1, res_sum = 0))
