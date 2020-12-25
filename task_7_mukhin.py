"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""

def pal_checker (string):
    dc_obj = DequeClass()
    newstring = string.replace (' ', '')
    for el in newstring:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc.obj.remove_from_front()
        last = dc.obj.remove_from_rear()
        if first != last:
            still_equal = False

        return still_equal

print (pal_checker ("молоко делили ледоколом")
       
