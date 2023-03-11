# Generated by Django 4.1.7 on 2023-03-08 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('img_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('preview', models.URLField(blank=True, null=True)),
                ('season', models.PositiveIntegerField()),
                ('series_number', models.PositiveIntegerField()),
                ('video_360', models.URLField(blank=True, null=True)),
                ('video_480', models.URLField(blank=True, null=True)),
                ('video_720', models.URLField(blank=True, null=True)),
                ('video_1080', models.URLField(blank=True, null=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(to='anime.genre'),
        ),
    ]