from django.contrib.auth.models import User
from django.db import models

from electrical_engineering.models import Product


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='Товар')
    text = models.TextField(verbose_name='Текст комментария')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user} {self.product} {self.date_added}'
