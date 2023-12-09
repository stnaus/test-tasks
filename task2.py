'''
Задание 2 Обработка входящего потока данных. 
Рекомендуется использовать регулярное выражение
Даны пути к файлам. Вывести в любом виде форматы относящиеся к форматам Excele используя регулярное выражение.
'''

import re


def find_excel_files(input_string):
    # Регулярное выражение для поиска файлов с расширениями форматов Excel
    pattern = r"\S+\.(?:xls[xm]?|XLS[XM]?|xls\*|vba)\b"

    # Находим все совпадения с помощью регулярного выражения
    matches = re.findall(pattern, input_string)

    # Возвращаем список найденных файлов
    return matches


# Пример передаваемой строки
file_paths = (
    '***\/Test/files/1.xls, ***\/Test/files/2.XLSX,***\/Test/files/9.vra, '
    '***\/Test/files/3.jpg, ***\/Test/files/4.xml, ***\/Test/files/5.png, '
    '***\/Test/files/6.xlsm, ***\/Test/files/7.xlso, ***\/Test/files/8.xls*, '
    '***\/Test/files/9.xlasx, ***\/Test/files/9.vba'
)

# Получаем пути к файлам формата Excel
excel_files = find_excel_files(file_paths)

# Выводим результат
print(','.join(excel_files))
