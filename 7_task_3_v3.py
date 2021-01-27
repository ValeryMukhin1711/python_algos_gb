"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import random
import operator
import timeit
import statistics 

def gnomeSort( arr_):
    arr = arr_.copy()
    i = 0
    n = len(arr)
    while i < n:
        if i == 0:
            i= i + 1
        if arr[i] >= arr[i - 1]:
            i = i + 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr

def sort_bubble(arr_1, direction = 'up' ):
    compare=operator.gt
    if direction == 'down':
        compare=operator.lt
    arr = arr_1.copy()
    i = 0
    while i  < len(arr):
        j = i
        while j < len(arr):
            if compare(arr[i],arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
            j +=1
        i +=1
    return arr
def my_med_sort_bubble(arr_1, direction = 'up' ):
    compare=operator.gt
    if direction == 'down':
        compare=operator.lt
    arr = arr_1.copy()
    i = 0
    while i  < len(arr):
        j = i +1
        while j < len(arr):
            if compare(arr[i],arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
            j +=1
        i +=1
    return arr[int(len(arr)/2)]

def my_med_for_sorted_arr (arr):
    n = len(arr)
    return arr[int(n/2)]

def my_med_sort_gnomeSort(arr_):
    arr = arr_.copy()
    i = 0
    n = len(arr)
    while i < n:
        if i == 0:
            i= i + 1
        if arr[i] >= arr[i - 1]:
            i = i + 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr[int(n/2)]

def my_med_1(arr):
    n = int(len(arr)/2)
    for i in arr:
        n_l = 0         
        for k in arr:
            if k < i :
                n_l +=1
        if n_l == n:
            break
    return i
run_time ={}  
m = int(input("Input odd number "))
lst =[]
for i in range(m):
    lst.append(int(random.random()*10*m))
print(f"original lst\t {lst}")  

lst_sorted = gnomeSort(lst)
lst_sort_bubble = sort_bubble(lst)

print(f"list_gnomeSort\t {lst_sorted}")
print(f"lst_sort_bubble\t {lst_sort_bubble}")
print("\nmedians")
my_med_sort_bubble
print(f"my_med_for_sorted_arr(lst_sorted) {my_med_for_sorted_arr(lst_sorted)}")
print(f"my_med_sort_gnomeSort(lst)\t  {my_med_sort_gnomeSort(lst)}")
print(f"my_med_sort_bubble(lst)\t\t  {my_med_sort_bubble(lst)}")
print(f"my_med_1(lst)\t\t\t  {my_med_1(lst)}")
print(f"statistics.median(lst)\t\t  {statistics.median(lst)}")

num = 10000
run_time["                   gnomeSort(lst)"] =str(timeit.timeit("gnomeSort(lst)", setup="from __main__ import (gnomeSort,lst)",number = num))+ ' sec'
run_time["                 sort_bubble(lst)"] =str(timeit.timeit("sort_bubble(lst)", setup="from __main__ import (sort_bubble,lst)",number = num))+ ' sec'
run_time["my_med_for_sorted_arr(lst_sorted)"] =str(timeit.timeit("my_med_for_sorted_arr(lst_sorted)", setup="from __main__ import (my_med_for_sorted_arr,lst_sorted)",number = num))+ ' sec'
run_time["       my_med_sort_gnomeSort(lst)"] =str(timeit.timeit("my_med_sort_gnomeSort(lst)", setup="from __main__ import (my_med_sort_gnomeSort,lst)",number = num))+ ' sec'
run_time["          my_med_sort_bubble(lst)"] =str(timeit.timeit("my_med_sort_bubble(lst)", setup="from __main__ import (my_med_sort_bubble,lst)",number = num))+ ' sec'
run_time["                    my_med_1(lst)"] =str(timeit.timeit("my_med_1(lst)", setup="from __main__ import (my_med_1,lst)",number = num))+ ' sec'
run_time["           statistics.median(lst)"] =str(timeit.timeit("statistics.median(lst)", setup="from __main__ import (statistics,lst)",number = num))+ ' sec'

print("\nresults test speed")
for i in run_time :
    print(i,end =' = ')
    print(run_time[i])
print(f"\noriginal lst\t {lst}")
