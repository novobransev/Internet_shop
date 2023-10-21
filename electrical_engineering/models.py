from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from profile_user.models import City


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'
        ordering = ['name']

    def __str__(self):
        return self.name


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ip адрес'
        verbose_name_plural = 'Ip адреса'

    def __str__(self):
        return self.ip


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL,
                                verbose_name='Страна производства')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    city_shop = models.ForeignKey(City, null=True, on_delete=models.SET_NULL,
                                  verbose_name='Город где находится товар')
    rating_products = models.FloatField(verbose_name='Рейтинг товара', default=None, blank=True, null=True,
                                        editable=False,  # Параметр, который делает поле скрытым
                                        validators=[
                                            MaxValueValidator(5),
                                            MinValueValidator(1)
                                        ])
    views = models.ManyToManyField(Ip, verbose_name="Просмотры", blank=True)

    class Meta:
        verbose_name = 'Электро товар'
        verbose_name_plural = 'Электро товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
