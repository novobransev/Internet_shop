"""
На этот файл можете внимания не обращать я нашел в интернете cities.json
но он не соответствовал стандартам django, поэтому я решил создать эту
программку для того чтобы он мне загрузил все города в бд
"""

import json

with open('counrties.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


with open('all_countries.json', 'w', encoding='utf-8') as outfile:
    count = 0
    outfile.write('[')

    for i in data.items():
        ing = {
            'pk': count,
            'model': 'electrical_engineering.Country',
            'fields': {'name': i[1]}
        }

        json.dump(ing, outfile, ensure_ascii=False)
        outfile.write(',')  # Добавляем запятую после каждой записи
        count += 1

    # После цикла удаляем последнюю запятую
    outfile.seek(outfile.tell() - 1)  # Перемещаем курсор на последний символ
    outfile.truncate()  # Усекаем содержимое файла после последнего символа

    outfile.write(']')
