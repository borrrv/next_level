from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from api.managers import CustomUserManager


class Contact(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(
        "Имя",
        max_length=50,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=50,
    )
    email = models.EmailField(
        "Электронная почта",
        max_length=254,
        unique=True,
    )
    phone_number = PhoneNumberField(
        "Номер телефона",
        unique=True,
        help_text=("Формат: +99999999999"),
    )
    password = models.CharField(
        "Пароль",
        max_length=100,
    )
    is_staff = models.BooleanField(
        ("Статус администратора"),
        default=False,
        help_text=(
            "Определяет, может ли пользователь войти на этот сайт "
            "с правами администратора."
        ),
    )
    is_active = models.BooleanField(
        ("Статус активности"),
        default=True,
        help_text=(
            "Указывает возможность пользователя войти на портал. "
        ),
    )
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "password",
        "first_name",
        "last_name",
        "phone_number",
    ]

    class Meta:
        ordering = ("id",)
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        constraints = [
            models.UniqueConstraint(
                fields=("email", "phone_number",),
                name="unique_email_and_phone_number"
            ),
        ]

    def __str__(self):
        return self.email
