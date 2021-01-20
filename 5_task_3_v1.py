"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
import string
import timeit

def fill_deque(st):
    d = deque(st)
    return d
def fill_list(st):
    l = list(st)
    return l

def add_r_deque(d,val):
    d.append(val)
    return d
def add_r_list(li,val):
    li.append(val)
    return li
def insert_deque(d,pos,val):
    d.insert(pos, val)
    return d
def insert_list(li,pos,val):
    li.insert(pos, val)
    return li
def count_deque(d,val):
    return d.count(val)
def count_list(li,val):
    return li.count(val)
'''
def slice_deque(d,pos_1,pos_2): - deque haven't slice method
    return d[pos_1:pos_2]
def slice_list(li,pos_1,pos_2):
    return li[pos_1: pos_2]
'''

test_string =  string.ascii_lowercase
my_d = deque(test_string)
my_list = list(test_string)


#Test 1 time for filling
print(f"my_list {my_list}")
print(f"my_d {my_d}")
print("\ntest filling")
print("list ",end='')
print(round(timeit.timeit("fill_list(test_string)", setup="from __main__ import (fill_list,   test_string)"),9))
print("deque ",end='')
print(round(timeit.timeit("fill_deque(test_string)", setup="from __main__ import (fill_deque,   test_string)"),9))            

my_d = deque(test_string)
my_list = list(test_string)            
  
#Test 2 add right

print("\ntest add right")
print("list ",end='')
print(round(timeit.timeit("add_r_list(my_list,'test')", setup="from __main__ import (add_r_list,   my_list)"),9))
print("deque ",end='')
print(round(timeit.timeit("add_r_deque(my_d,'test')", setup="from __main__ import (add_r_deque,   my_d)"),9))

my_d = deque(test_string)
my_list = list(test_string)

#Test 3 insert pos 10
print("\ntest insert pos = 10")
print("list ",end='')
print(round(timeit.timeit("insert_list(my_list,10,'test')", setup="from __main__ import (insert_list,   my_list)",number = 100000),9))
print("deque ",end='')
print(round(timeit.timeit("insert_deque(my_d,10,'test')", setup="from __main__ import (insert_deque,   my_d)",number =100000),9))


#Test 4 count x
my_d = deque(test_string)
my_list = list(test_string)

print("\ntest count  = 't'")
print("list ",end='')
print(round(timeit.timeit("count_list(my_list,'t')", setup="from __main__ import (count_list,   my_list)"),9))
print("deque ",end='')
print(round(timeit.timeit("count_deque(my_d,'t')", setup="from __main__ import (count_deque,   my_d)"),9))





