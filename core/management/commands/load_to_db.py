from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):

        subprocess.call("python manage.py loaddata categories.json", shell=True)
        print("Категории успешно добавлены в базу данных")
        subprocess.call("python manage.py loaddata all_countries.json", shell=True)
        print("Страны успешно добавлены в базу данных")
        subprocess.call("python manage.py loaddata all_cities.json", shell=True)
        print("Города успешно добавлены в базу данных")
