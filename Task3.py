# Пример 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# start_list = list(map(float, input("Введите числа через пробел:\n").split()))   # 1.1 1.2 3.1 5 10.01
# diff_max_min_list = []
# for i in start_list:
#     if i%1 != 0:
#         diff_max_min_list.append(round(i%1,2))
# print(f'{diff_max_min_list} - дробные части элементов с округлением до 2 знаков после запятой')
# print(f'{max(diff_max_min_list)} - максимальное значение дробной части элементов')
# print(f'{min(diff_max_min_list)} - минимальное значение дробной части элементов')
# print(f'{max(diff_max_min_list)-min(diff_max_min_list)} - разницa между максимальным и минимальным значением дробной части элементов')


start_list = list(map(float, input("Введите числа через пробел:\n").split())) # 1.1 1.2 3.1 5 10.01
diff_max_min_list = list(x % 1 for x in start_list if x % 1 != 0)
diff_max_min_list = list(round(x, 2) for x in diff_max_min_list)
print(max(diff_max_min_list) - min(diff_max_min_list))
