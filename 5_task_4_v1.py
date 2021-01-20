"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
import string
import timeit
from random import randint

def unsort (li):
    res_li = ''
    while li :
        res_li += li.pop(randint(0,len(li)-1))
    return res_li

def fill_ord_dict(my_dict):
    ord_dict = collections.OrderedDict(my_dict)
    return ord_dict

def sort_dict(d):
    res_d ={}
    list_keys = list(d.keys())
    list_keys.sort()
    for i in list_keys:
        res_d[i] = d[i]
    return res_d
def move_ord_d(ord_d, key): 
    ord_d.move_to_end(key,last =True)
    ord_d.move_to_end(key,last =False) # return to the initial conditions
    return ord_d

def move_st_d(d,key):
    t = {key:d.pop(key)}
    t.update(d)
    d = {key:t.pop(key)} # return to the initial conditions
    t.update(d)
    return t

   
    

test_string =  string.ascii_lowercase
my_list = list(test_string)
my_list = unsort(my_list)
my_dict = {}
d = {}
sorted_dict ={}
i = 0 
while i < len(my_list):
#    print(f"{i} {my_list[i]}")
    my_dict[my_list[i]] = i
    d[my_list[i]] = i
    i +=1
print("d")
print(d)

new_d =  move_st_d(d,'x')

print("new_d")
print(new_d)
  
ord_dict = collections.OrderedDict(my_dict)
ord_dict_sorted = collections.OrderedDict(sorted(my_dict.items()))

print("\move to end ord_dict")
print(ord_dict)
print("\nmy_dict")
print(my_dict)
sorted_dict = sort_dict(my_dict)
print("\nsorted_dict")
print(sorted_dict)


print("\nmove ord_dict last first ",end='')
print(round(timeit.timeit("move_ord_d(ord_dict, 'x')", setup="from __main__ import (move_ord_d, ord_dict, collections)"),9))            
print("\nmove std_dict last first ",end='')
print(round(timeit.timeit("my_dict = move_st_d(my_dict,'x')", setup="from __main__ import (move_st_d, my_dict, collections)"),9))            


#Test make orderdict
print("\nfunction fill_ord_dict ",end='')
print(round(timeit.timeit("fill_ord_dict(my_dict)", setup="from __main__ import (fill_ord_dict, my_dict)"),9))
print("\nord_dict = collections.OrderedDict(my_dict)",end='')
print(round(timeit.timeit("ord_dict = collections.OrderedDict(my_dict) ", setup="from __main__ import (fill_ord_dict, my_dict, collections)"),9))            
print("\nord_dict")
print(ord_dict)
print("\nord_dict_sorted = collections.OrderedDict(sorted(my_dict.items())) ",end='')
print(round(timeit.timeit("ord_dict_sorted = collections.OrderedDict(sorted(my_dict.items()))", setup="from __main__ import (fill_ord_dict, my_dict, collections)"),9))            
print("\nsorted ord_dict")
print(ord_dict_sorted)
print("\nsorted_dict ",end='')
print(round(timeit.timeit("sorted_dict = sort_dict(my_dict)", setup="from __main__ import (sort_dict, my_dict, collections)"),9))            
print("\nsorted_dict")
print(sorted_dict)

