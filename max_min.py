# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_my = [1.1, 1.2, 3.1, 5, 10.01]
print(list_my)

max_element = list_my[0]%1
# max_index = 0

min_element = list_my[0]%1
# min_index = 0

for i in range(0, len(list_my)): # с 1, т.к. 0 объявлен
    # print(list_my[i])
    if max_element < list_my[i]%1:
        max_element = list_my[i]%1
    if (min_element > list_my[i]%1) and (list_my[i]%1>0)  :
        min_element = list_my[i]%1

result = max_element-min_element
print(round(result,3))



