# Generated by Django 4.1.7 on 2023-03-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to='profiles/', verbose_name='Фото'),
        ),
    ]
