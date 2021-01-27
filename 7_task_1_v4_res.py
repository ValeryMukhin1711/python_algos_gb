"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""


import random
import operator
import timeit

def sort_arr(arr_1, direction = 'up' ):
    compare=operator.gt
    if direction == 'down':
        compare=operator.lt
    
    arr= arr_1.copy()
    i = 0
    while i  < len(arr):
        j = i+1
        while j < len(arr):
            if compare(arr[i],arr[j]): 
                arr[i],arr[j] = arr[j],arr[i]
            j +=1
        i +=1
    return arr

def sort_arr_short_print(arr_1, direction = 'up' ):
    compare=operator.gt
    if direction == 'down':
        compare=operator.lt
    arr = arr_1.copy()
    i = 0
    while i  < len(arr):
#        print(f"i = {i}")
        j = i
        k = 0
        while j < len(arr):
            
            if compare(arr[i],arr[j]):
                k = 1
                arr[i],arr[j] = arr[j],arr[i]
            j +=1
        if k == 0:
            print(f"Break i ={i} j = {j}")
            break
        i +=1
    return arr

def sort_arr_short(arr_1, direction = 'up' ):
    compare=operator.gt
    if direction == 'down':
        compare=operator.lt
    arr = arr_1.copy()
    i = 0
    while i  < len(arr):
        j = i
        k = 0
        while j < len(arr):
            
            if compare(arr[i],arr[j]):
                k = 1
                arr[i],arr[j] = arr[j],arr[i]
            j +=1
        if k == 0:
           #  print(f"Break i ={i} j = {j}")
             break    
        i +=1
    return arr

lst = []
n = 200
for i in range(n):
    lst.append(int(random.random()*n - n/2))
print(f"lst {len(lst)}\n{lst}\n")
print(f"sort_arr(lst,'up') {len(sort_arr(lst,'up'))}\n{sort_arr(lst,'up')}\n")
print(f"sort_arr(lst,'down') {len(sort_arr(lst,'down'))}\n{sort_arr(lst,'down')}\n")
print(f"sort_arr_short(lst,'up') {len(sort_arr_short(lst,'up'))}\n{sort_arr_short_print(lst,'up')}\n")
print(f"sort_arr_short(lst,'down') {len(sort_arr_short(lst,'down'))}\n{sort_arr_short_print(lst,'down')}\n")
print(f"lst {len(lst)}\n{lst}")
run_time={}
num = 100
run_time["sort_arr(lst,'up'))"] =str(timeit.timeit("sort_arr(lst,'up')", setup="from __main__ import (sort_arr,lst)",number = num))+ ' sec'
run_time["sort_arr(lst,'down'))"] =str(timeit.timeit("sort_arr(lst,'down')", setup="from __main__ import (sort_arr,lst)",number = num))+ ' sec'
run_time["sort_arr_short(lst,'up'))"] =str(timeit.timeit("sort_arr_short(lst,'up')", setup="from __main__ import (sort_arr_short,lst)",number = num))+ ' sec'
run_time["sort_arr_short(lst,'down'))"] =str(timeit.timeit("sort_arr_short(lst,'down')", setup="from __main__ import (sort_arr_short,lst)",number = num))+ ' sec'

print("\nresults test speed")
for i in run_time :
    print(i,end =' = ')
    print(run_time[i])



