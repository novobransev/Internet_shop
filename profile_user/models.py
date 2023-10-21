from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
     Это новая модель про информацию user, пока что не хочу расширять AbstractUser
     ибо с ним есть небольшая проблема с хранением пароля и с этим же я не могу
     сбрасывать пароль!
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(null=True, blank=True, verbose_name='Биография')
    profile_pic = models.ImageField(null=True, blank=True, verbose_name='Аватарка', upload_to="images/profile/")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Город')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

