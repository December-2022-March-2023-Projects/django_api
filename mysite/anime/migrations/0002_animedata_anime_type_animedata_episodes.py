# Generated by Django 4.0.3 on 2022-12-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animedata',
            name='anime_type',
            field=models.CharField(default='series', max_length=20),
        ),
        migrations.AddField(
            model_name='animedata',
            name='episodes',
            field=models.IntegerField(default=0),
        ),
    ]
