#  Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (In
#tel)] on win32
# Win7

#Unfortunately my IDLE does not support Russian, so the analytics are in separate file named 6_task_1_v1.txt

mem_usage ={}
run_time ={}
import memory_profiler
mem_usage ['import memory_profiler'] = str(memory_profiler.memory_usage()) + ' Mib'
from collections import deque
mem_usage ['import deque'] = str(memory_profiler.memory_usage()) + ' Mib'
import timeit
mem_usage ['import timeit'] = str(memory_profiler.memory_usage()) + ' Mib'

def sum_h_1(a,b,x):

    h_l =('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    if h_l.index(a) + h_l.index(b) + h_l.index(x) > 15:
        return list('1'+ h_l[h_l.index(a)+h_l.index(b)+int(x) - 16])
    else:
        return list('0' + h_l[h_l.index(a) + h_l.index(b)+int(x)])
mem_usage ['def sum_h_1'] = str(memory_profiler.memory_usage()) + ' Mib'

def sum_h_2(a,b, x='0'):
    a = list(a)
    b = list(b)
    r = deque()
    if len(b) > len(a):
        a,b = b,a
    while a:
        t_a = a.pop()
        if b:
            t_b = b.pop()
            x,y = sum_h_1(t_a,t_b,x)
            r.appendleft(y)
        else:
            x,y = sum_h_1(t_a,'0',x)
            r.appendleft(y)
    if x =="1" :r.appendleft(x)        
    return ''.join(r)
mem_usage ['def sum_h_2'] = str(memory_profiler.memory_usage()) + ' Mib'
def mult_h_1 (a,b):
    h_l =('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
#    a = list(a)
    idx_a = h_l.index(a)
    i = 0
    r = ""
    while i < h_l.index(a):
        r = sum_h_2(r,b)
        i +=1
    return r

mem_usage ['def mult_h_1'] = str(memory_profiler.memory_usage()) + ' Mib'

def mult_h_2 (a,b):
    h_l =('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    a = list(a)
    s = ""
    k = 0
    while a:
        t_a = a.pop()
        idx_a = h_l.index(t_a)
        i = 0
        r = ""
        
        while i < h_l.index(t_a):
            r = sum_h_2(r,b)
            i +=1
        j = 0    
        while j < k:
            r = r + '0'
            j +=1
        s = sum_h_2(r,s)
        k +=1
        
    return s

mem_usage ['def mult_h_2 '] = str(memory_profiler.memory_usage()) + ' Mib'
n = 1000 
mem_usage [f"declare n = {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
my_list = list(range(n))
mem_usage [f"make list {n}"] = str(memory_profiler.memory_usage()) + ' Mib'
print(my_list)
mem_usage ['print my_list '] = str(memory_profiler.memory_usage()) + ' Mib'

n = 1000000 
mem_usage [f"declare n= {n} "] = str(memory_profiler.memory_usage()) + ' Mib'
my_list = list(range(n))
mem_usage [f"make list {n} "] = str(memory_profiler.memory_usage()) + ' Mib'


print(str(sum_h_1('F','A','0')))
run_time["sum_h_1('F','A')"] =str(timeit.timeit("sum_h_1('F','A','0')", setup="from __main__ import (sum_h_1)",number = 1000))+ ' sec'
mem_usage [f"timeit.timeit(sum_h_1('F','A','0')  "] = str(memory_profiler.memory_usage()) + ' Mib'
print(str(sum_h_2('1178','8A')))
run_time["sum_h_2('1178','8A')"] =str(timeit.timeit("sum_h_2('1178','8A')", setup="from __main__ import (sum_h_2)",number = 1000))+ ' sec'
print()



print(mult_h_1('2','A1'))
run_time["mult_h_1('2','A1'))"] =str(timeit.timeit("mult_h_1('2','A1')", setup="from __main__ import (mult_h_1)",number = 1000)) + ' sec'
print(mult_h_2('1111','1A'))
run_time["mult_h_2('1111','1A'))"] =str(timeit.timeit("mult_h_2('1111','1A')", setup="from __main__ import (mult_h_2)",number = 1000))+ ' sec'
print("\nmemory usage accumulation")
for i in mem_usage:
    print(i,end ='')
    print(mem_usage[i])
print("\nresults test speed")
for i in run_time :
    print(i,end ='  ')
    print(run_time[i])
    
