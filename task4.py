'''
Задание 4  Запрос данных на сервер и их вывод в нужном формате:
Используя саййт  https://terrikon.com/football/italy/championship/ сделать скрипт, который   достаёт данные из таблицы с игроками по забитым голам  в нужном формате:
Пример формата данных:
<table><th></th><th>Игрок</th><th>Команда</th><th>Забито</th><th>Игр</th><th>Среднее</th><tr><td>1.</td><td>Осимхен</td><td>Наполи</td><td>23</td><td>30</td><td>0.77…
</table>.
Вывести данные можно в отдельную переменную.
'''

import requests
from bs4 import BeautifulSoup


def fetch_player_data(url, html):
    # Получаем содержимое веб-страницы
    response = requests.get(url)

    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим таблицу по ее id
        table = soup.find(
            'div', id='champs-strikers').find('table', class_='colored')

        # Проверяем, что таблица найдена
        if table:
            if html:
                formatted_data = "<table>"
                formatted_data += "<th></th><th>Игрок</th><th>Команда</th><th>Забито</th><th>Игр</th><th>Среднее</th>"

                # Итерируемся по строкам (теги <tr>) таблицы
                for row in table.find_all('tr')[1:]:
                    # Формируем строку для каждой строки таблицы
                    formatted_data += "<tr>"
                    # Итерируемся по ячейкам (теги <td>) текущей строки
                    for cell in row.find_all('td'):
                        # Добавляем содержимое ячейки в таблицу
                        formatted_data += "<td>" + \
                            str(cell.get_text(strip=True)) + "</td>"
                    # Закрываем строку
                    formatted_data += "</tr>"

                # Закрываем таблицу
                formatted_data += "</table>"

                return formatted_data
            else:
                # Инициализируем пустой список для хранения данных
                data = []

                # Итерируемся по строкам (теги <tr>) таблицы
                for row in table.find_all('tr'):
                    # Инициализируем пустой список для хранения данных строки
                    row_data = []

                    # Итерируемся по ячейкам (теги <td>) текущей строки
                    for cell in row.find_all('td'):
                        # Добавляем содержимое ячейки в список данных строки
                        row_data.append(cell.get_text(strip=True))

                    # Добавляем данные строки в общий список данных
                    data.append(row_data)

                head_data = []
                for cell in table.find('tr').find_all('th'):
                    head_data.append(cell.get_text(strip=True))

                data[0].extend(head_data)

                return data
        else:
            print("Таблица не найдена.")
    else:
        print("Ошибка при получении данных")
        return None


if __name__ == "__main__":
    url = "https://terrikon.com/football/italy/championship/"
    
    # Можно вернуть данные в виде списка или в виде строки, содержащей html-таблицу
    player_data = fetch_player_data(url, html=False)

    if player_data:
        print(player_data)
    else:
        print('Что-то пошло не так')
