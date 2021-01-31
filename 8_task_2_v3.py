"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

import collections

nodes ={}

class Node:
    nodes.clear()
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_all_Nodes(self):
        print('\n\tAll nodes')
        for i in nodes:
            print(f'{i}\t {nodes[i]}')
        return
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            nodes[data] = Node(data)
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def totalTree_d(self,d ={},i = 0):
        i += 1        
        if self.left:
            self.left.totalTree_d(d,i)
        d[self.data] = i            
        if self.right:
            self.right.totalTree_d(d,i)
        return d

    def print_Tree(self):
        print('------- Tree Structure --------')
        temp_d = self.totalTree_d(d ={})
        len_d = len(temp_d)
        h_tree  = max(temp_d.values())
        j = 0
        while j <= h_tree:
            pos = 0
            m = 0
            for k in self.totalTree_d(d ={}):
                pos += 1
                if temp_d[k] == j:
                   # m = 0
                    while m < pos:
                        print('  ',end='')
                        m +=1
                    print(f'{k}',end='')
            print()
            j +=1
        print('-------------------------------')
        return    



root = Node(12)
root.insert(3)
root.insert(6)
root.insert(14)
root.insert(15)
root.insert(13)
root.insert(8)
root.insert(2)

print(f'\nnodes values and levels {root.totalTree_d()}\n') 
root.print_Tree()

root.print_all_Nodes()

while 1:
    inp = (input("\nInput root value for next Tree or space for exit "))
    if inp =='':
        print('Good By!')
        break
    root = Node(int(inp))
    inp = input('Input values for nodes separated by space ')
    lst =[]
    for i in (inp.split()):
        lst.append(int(i))
    for i in lst:
        root.insert(i)
    print(f'\nnodes values and levels {root.totalTree_d()}\n')   
    root.print_Tree()
    root.print_all_Nodes()
