"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

import heapq  
from collections import Counter  
from collections import namedtuple


class Node:
    def __init__(self, left, right ):
        self.left = left
        self.right = right

    def pass_tree(self, code, acc):
       
        self.left.pass_tree(code, acc + "0")
        self.right.pass_tree(code, acc + "1")         
     
class Leaf:
    def __init__(self, char):
        self.char = char
    def pass_tree(self, code, acc):
        
        code[self.char] = acc or "0"
class Leaf_1:
    def __init__(self, char):
        self.char = char
    def pass_tree(self, code, acc):
        
        code[self.char] = acc or "0"         

def huff_(s): 
    h = []
    h1 = {}
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
        h1[ch] = (freq,len(h1),Leaf_1(ch))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1: 
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right))) 
        count += 1  
    code = {}

    if h: 
        [(_freq, _count, root)] = h
        root.pass_tree(code, "") 
    return code  
 
def use_coder(s):
    code = huff_(s) 
    encoded = "".join(code[ch] for ch in s)
    print(Counter(s).items())
    print()
    for i in code:
        print(f'{i} <-> {code[i]}')
    print()    
    print(s,end =' <-> ') 
    print(encoded)  



#s = input('Input string')
s = 'beep boop beer!'
code = huff_(s)
print(f' test string "{s}"')
print(Counter(s).items())
encoded = "".join(code[ch] for ch in s)  

print()
for i in code:
    print(f'{i} <-> {code[i]}')
print()    

print(s,end =' <-> ') 
print(encoded)  


while 1:
    s = input('Input next string or nothing for exit ')
    if s =='': break
    use_coder(s)
    
    
