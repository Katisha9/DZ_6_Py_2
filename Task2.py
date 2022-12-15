# Пример 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# from random import randint as rand
#
# size = int(input('Введите длину списка: '))
# start_list = []
#
# for i in range(size):
#     start_list.append(rand(0, 10))
# print(start_list)
#
# pair_list = []
#
# for i in range(int(size/2)):
#     pair_list.append(start_list[i] * start_list[-i-1])
# print(pair_list)



import random

size = int(input('Введите длину списка: '))
start_list = [random.randint(0, 10) for i in range(size)]
print(start_list)

pair_list = [start_list[i] * start_list[-i - 1] for i in range(int(size / 2))]
print(pair_list)