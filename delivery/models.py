from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .user_manager import UserManager

class User(AbstractUser, PermissionsMixin):

    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=225)
    balance = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'

class Staff(User):

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Customer(User):

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Courier(User):

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    avaiable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class OrderBox(models.Model):
    user = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(verbose_name='Total Price')
    ordered_at = models.DateTimeField(auto_now_add=True)
