'''
Задание 3 Обработка входящего потока данных.
Рекомендуется использовать регулярное выражение
Реализовать консольный скрипт, который в качестве параметра будет принимать строку из разделенных между собой натуральных чисел.
//Выводит этот же массив отсортированный в порядке возрастания.
Во входной строке числа разделены как минимум одним пробелом, в сортировке участвуют только числа
'''

import sys
import re


def sort_numbers(input_string):
    # Используем регулярное выражение для извлечения только чисел из строки
    numbers = re.findall(r'-?\d+', input_string)

    # Преобразуем строки в числа и создаем множество для уникальных значений
    unique_numbers = set(map(int, numbers))
    
    # Преобразуем обратно в список и сортируем
    sorted_unique_numbers = sorted(unique_numbers)

    # Выводим отсортированный массив чисел
    print(' '.join(map(str, sorted_unique_numbers)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Используйте скрипт следующим образом: python task3.py 'числа_разделенные_пробелами'")
    else:
        input_string = sys.argv[1]
        sort_numbers(input_string)
