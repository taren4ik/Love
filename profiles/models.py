from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

CHOICES = (
    ('Vladivostok', 'Владивосток'),
    ('Artem', 'Артем'),
    ('Nakhodka', 'Находка'),
    ('Ussuriysk', 'Уссурийск'),
)
CHOICES_SEX = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    name = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='Владелец профайла',
                                related_name='profiles',
                                null=True, )

    phone = PhoneNumberField(null=False, unique=True)
    image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        verbose_name='Фото профиля',
    )

    description = models.TextField(
        blank=True, verbose_name='Описание анкеты'
    )

    year = models.PositiveSmallIntegerField(
        db_index=True,
        validators=[MaxValueValidator(date.today().year - 18)],
        verbose_name='Год рождения',
        default=date.today().year - 18
    )

    city = models.CharField(
        max_length=16,
        choices=CHOICES,
        default='Vladivostok',
        verbose_name='Город проживания',
    )

    sex = models.CharField(
        max_length=1,
        choices=CHOICES_SEX,
        default='Male',
        verbose_name='Пол',
    )

    category = models.ForeignKey(
        Category, null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='titles'
    )

    def get_absolute_url(self):
        return reverse('profiles:profile_detail',
                       kwargs={'profile_id': self.pk})

    class Meta:
        # ordering = ('name',)
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

    def __str__(self):
        return f'Name {self.name}, phone: {self.phone}, born: {self.year}'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
        help_text="Пользователь, который подписывается",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Профиль",
        help_text="Профиль, на который подписываются",
    )

    def __str__(self):
        return self.user
