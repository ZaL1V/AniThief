# Generated by Django 4.1.4 on 2023-03-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_anime_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(blank=True, to='anime.genre'),
        ),
    ]
