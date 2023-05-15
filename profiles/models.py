from datetime import date

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

CHOICES = (
    ('Vladivostok', 'Владивосток'),
    ('Artem', 'Артем'),
    ('Nakhodka', 'Находка'),
    ('Ussuriysk', 'Уссурийск'),
)
CHOICES_SEX = (
    ('M', 'Мужской'),
    ('F', 'Женский'),
)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    phone = PhoneNumberField(
        null=False,
        unique=True,
        verbose_name='Телефон',)

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
        related_name='users'
    )

    avatar = models.ImageField(
        blank=True,
        verbose_name='Аватар профиля',
        null=False,
    )



    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'year', 'sex', 'city']

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
        ordering = ['-id']

    def __str__(self):
        return f'Name {self.username}, phone: {self.phone}, born: {self.year}'

    def get_absolute_url(self):
        return reverse('profiles:profile_detail',
                       kwargs={'profile_id': self.pk})


class Photo(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='image', verbose_name='Фото',)

    image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        verbose_name='Фото',)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Follow(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
        help_text="Пользователь, который подписывается",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Профиль",
        help_text="Профиль, на который подписываются",
    )

    def __str__(self):
        return f'Name {self.user}'


class Comment(models.Model):
    profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Комментатор",
        help_text="Автор коммента",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="Автор",
        help_text="Автор анкеты",
    )

    text = models.TextField(
        verbose_name="Комментарий",
        help_text="Текст комментария", )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата размещения",
        help_text="Дата размещения комментария",
    )

    def __str__(self):
        count_symbol = 15
        return self.text[:count_symbol]


class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sender",
        verbose_name="Получатель",
        help_text="Получатель сообщения",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="answer",
        verbose_name="Отправитель сообщения",
        help_text="Отправитель",
    )

    text = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата отправки",
        help_text="Дата отправки сообщения",
    )
