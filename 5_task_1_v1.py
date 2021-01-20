"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""




from collections import defaultdict

d_dict = defaultdict(list)

while 1 :
    company_name = input("input next company name or nothing ")
    if company_name != "":
        quaters =input ("input profit by quarter separeted by space ").split()
        if len(quaters) != 4:
            print("Value Error: input FOUR numbers for FOUR quarter")
            continue
        else:
            try :
                for i in quaters:
                    a = int(i)
            except :
                print("Type Error: input DIGIT as profits")
                continue
        s = 0   
        for i in quaters :
            d_dict[company_name].append(int(i))
            s += int(i)
        d_dict[company_name].append(s)   
    else: break
print(d_dict)
sum = 0
for i in d_dict:
    sum += d_dict[i][4]
avg_prf = sum/len(d_dict)
print(f"Total profit for all company {sum}, Average profit {round(avg_prf,2)}")
print(f"Company with profit more than average",end="")
for i in d_dict:
    if d_dict[i][4] > avg_prf :
        print(f" '{i}' ",end='')
print()        
print(f"Company with profit equal or less than average",end="")
for i in d_dict:
    if d_dict[i][4] <= avg_prf :
        print(f" '{i}' ",end='')

    
