from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from electrical_engineering.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


class Rating(models.Model):
    estimation = models.PositiveIntegerField(verbose_name='Оценка товара', default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    from_product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = ('user', 'from_product')

    def __str__(self):
        return (f"estimation={self.estimation};user={self.user};from_product={self.from_product};"
                f"id={self.from_product.id}")


@receiver(post_save, sender=Rating)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        req = str(instance)
        dictionary = dict(subString.split("=") for subString in req.split(";"))

        all_ratings = Rating.objects.filter(from_product=dictionary['id']).all()

        summa = []
        count = 0
        for i in all_ratings:
            d = dict(subString.split("=") for subString in str(i).split(";"))
            summa.append(int(d['estimation']))
            count += 1

        result = sum(summa) / count

        update_product = Product.objects.get(id=dictionary['id'])
        update_product.rating_products = result
        update_product.save()

