# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_my = [2, 3, 4, 5, 6]
print(list_my)

left_element = 0
right_element = len(list_my) - 1

list_proizvedenie = []

while left_element <= right_element:
   list_proizvedenie.append(list_my[left_element] * list_my[right_element])
   left_element = left_element + 1
   right_element = right_element - 1

print(list_proizvedenie)