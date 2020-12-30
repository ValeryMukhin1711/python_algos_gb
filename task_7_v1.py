"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def if_true(n, i = 0, sum_row = 0):
    if n+1 == i:
        if sum_row == n*(n+1)/2:
            print(f"n = {n} sum_row {sum_row}")
            print(f"n = {n} n*(n+1)/2 {n*(n+1)/2}")
            return True
        else :
            print(f"2 sum_row {sum_row}")
            print(f"2 n*(n+1)/2 {n*(n+1)/2}")
            return False
    else :
        sum_row = sum_row + i
        i +=1
    return if_true(n,i, sum_row)    



str = input("Input number ")
try:
    numb = int(str)
except:
    print("Error! Input number")

print(if_true(numb))
