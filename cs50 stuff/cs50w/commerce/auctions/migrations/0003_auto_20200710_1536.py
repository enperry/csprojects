# Generated by Django 3.0.8 on 2020-07-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20200710_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(max_length=900),
        ),
    ]
