"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random

def guess (n_attemp, x):
    if n_attemp > 10:
        print (f"& was {x}")
        return x
    else:
        while True:
            try:
                y = int(input("input number "))
                break
            except:
                print("Your input isn't digital ")
# n_attemp +=1
    if y ==x:
        print ("Bingo! Correct number! ")
    elif y > x:
        print (f"Your number {y} is greater than X ")
        return guess (n_attemp +1, x)
    else:
        print (f"Your number {y} is less than X ")
        return guess (n_attemp +1, x)

x = random.randint (0, 100)
#print (x)

guess (1, x)

