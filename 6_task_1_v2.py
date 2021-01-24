#  Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (In
#tel)] on win32
# Win7

#Unfortunately my IDLE does not support Russian, so the analytics are in separate file named 6_task_1_v2.txt


mem_usage ={}
run_time ={}
import memory_profiler
mem_usage ['import memory_profiler'] = str(memory_profiler.memory_usage()) + ' Mib'
from collections import deque
mem_usage ['import deque'] = str(memory_profiler.memory_usage()) + ' Mib'
import timeit
mem_usage ['import timeit'] = str(memory_profiler.memory_usage()) + ' Mib'

def test_func_for_dict(d):
    t_d = {}
    for i in d:
        t_d[i] = i*2
    return t_d

def test_func_for_list(lst):
    t_lst = []
    for i in lst:
        t_lst.append(i*2)
    return t_lst    
    

n = 1000
mem_usage [f"declare n= {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
lst_1 = list(range(n))
mem_usage [f"make lst_1 {n} "] = str(memory_profiler.memory_usage()) + ' Mib'

dict_1 ={}
for i in range(n):
    dict_1[i] = 2*i
mem_usage [f"make dict_1 {n} "] = str(memory_profiler.memory_usage()) + ' Mib' 
dict_2 = test_func_for_dict(dict_1)
mem_usage [f"make dict_2 {n} "] = str(memory_profiler.memory_usage()) + ' Mib' 

n = 1000000
mem_usage [f"declare n= {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
lst_2 = list(range(n))
mem_usage [f"make lst_2 {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
lst_3 = test_func_for_list(lst_2)
mem_usage [f"make lst_3 {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
dict_2 ={}
for i in range(n):
    dict_2[i] = 2*i
mem_usage [f"make dict_2 {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
dict_3 = test_func_for_dict(dict_2)
run_time["test_func_for_list(lst_2)"] =str(timeit.timeit("test_func_for_list(lst_2)", setup="from __main__ import (test_func_for_list,lst_2)",number = 100))+ ' sec'
mem_usage [f"make dict_3 {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
run_time["test_func_for_dict(dict_2)"] =str(timeit.timeit("test_func_for_dict(dict_2)", setup="from __main__ import (test_func_for_dict,dict_2)",number = 100))+ ' sec'


print("\nmemory usage accumulation")
for i in mem_usage:
    print(i,end ='')
    print(mem_usage[i])

print("\nresults test speed")
for i in run_time :
    print(i,end ='  ')
    print(run_time[i])
    
