"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""



from collections import deque


#h_l =('1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')

def sum_h_1(a,b,x):
    h_l =('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    if h_l.index(a) + h_l.index(b) + h_l.index(x) > 15:
        return list('1'+ h_l[h_l.index(a)+h_l.index(b)+int(x) - 16])
    else:
        return list('0' + h_l[h_l.index(a) + h_l.index(b)+int(x)])

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

def mult_h_one_digit (a,b):
    h_l =('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    idx_a = h_l.index(a)
    i = 0
    r = ""
    while i < h_l.index(a):
        r = sum_h_2(r,b)
        i +=1
    return r
def mult_hex (a,b):
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



print(mult_h_one_digit('2','A1'))
print(mult_hex('FFF111','1A'))


