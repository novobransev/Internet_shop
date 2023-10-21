from django.contrib.auth.models import User
from django.db import models
from electrical_engineering.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзину'
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user} {self.product}'
