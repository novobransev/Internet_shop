"""
На этот файл можете внимания не обращать я нашел в интернете cities.json
но он не соответствовал стандартам django, поэтому я решил создать эту
программку для того чтобы он мне загрузил все города в бд
"""

import json

with open('cities.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


with open('all_cities.json', 'w', encoding='utf-8') as outfile:
    count = 0
    outfile.write('[')

    for i in data['city']:
        ing = {
            'pk': count,
            'model': 'profile_user.City',
            'fields': {'name': i['name']}
        }

        json.dump(ing, outfile, ensure_ascii=False)
        outfile.write(',')  # Добавляем запятую после каждой записи
        count += 1

    # После цикла удаляем последнюю запятую
    outfile.seek(outfile.tell() - 1)  # Перемещаем курсор на последний символ
    outfile.truncate()  # Усекаем содержимое файла после последнего символа

    outfile.write(']')
